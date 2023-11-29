from dataclasses import dataclass, asdict
from typing import Any, Literal
from datetime import datetime
from colorama import Fore
import pretty_tables
import json
import os


# Path to the JSON file
data_path: str = f"{os.path.expanduser('~/documents')}/.todos.json"



# Task class
@dataclass(frozen=False, order=True)
class Task:
    id: int = 1
    name: str = ''
    done: bool = False
    created_at: str = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    done_at: str = ''
        

    def open_or_create(self, todos = None) -> (Any | Literal[False] | None):

        # Read all todos
        if todos is None:
            if os.path.exists(data_path):
                with open(data_path, 'r') as todos:
                    tasks = json.load(todos)
                    return tasks
                
        # Create a todo
        else:
            if not os.path.exists(data_path):

                with open(data_path, 'w+') as todos:

                    task = [asdict(self)]
                    json.dump(task, todos, indent=4)

            elif os.path.exists(data_path):

                with open(data_path, 'r+') as todos:

                    try:
                        tasks = json.load(todos)
                        self.id = tasks[-1]['id'] + 1
                        tasks.append(asdict(self))
                        todos.seek(0)
                        todos.truncate()
                        json.dump(tasks, todos, indent=4)

                    except IndexError:
                        tasks = json.load(todos)
                        tasks.append(asdict(self))
                        todos.seek(0)
                        todos.truncate()
                        json.dump(tasks, todos, indent=4)

                    except json.JSONDecodeError:
                        tasks = []
                        self.id = 1
                        tasks.append(asdict(self))
                        todos.seek(0)
                        todos.truncate()
                        json.dump(tasks, todos, indent=4)


    def printTodos(self):
        """Read your todo's and display it to the CLI
        """

        # Clear the cli before printing out the table

        headers = ["Nº", "Name", "Done?", "Created at", "Completed at"]
        rows = []
        total_pending = 0

        try:
            for todo in self.open_or_create():

                if not todo['done']:
                    todo['done'] = ' No'
                    total_pending += 1 
                else:
                    todo['done'] = " \u2705"

                if not todo['done_at']:
                    todo['done_at'] = 'Not completed yet.'

                rows.append([todo['id'], todo['name'], todo['done'], todo['created_at'], todo['done_at']])

        except (TypeError, json.JSONDecodeError):

            # No todos found or json file found - Populate with -
            rows.append(['-', '-', '-', '-', '-'])


        colors = [
            pretty_tables.Colors.bold,
            pretty_tables.Colors.cyan,
            pretty_tables.Colors.cyan,
            pretty_tables.Colors.bold,
            pretty_tables.Colors.bold,
        ]

        table = pretty_tables.create(
            headers=headers,
            rows=rows,
            empty_cell_placeholder='--',
            colors=colors, 
        )


        for _ in range(2):
            print()

        print(table)
        print()
        print(Fore.RED + '-'*67)
        print(Fore.WHITE + f'| Total pending tasks ... > {str(total_pending)} {" "*36} |')
        print(Fore.RED + '-'*67)

        for _ in range(2):
            print(Fore.RESET + '')


    def add(self):
        """Add todo's to your list
        """
        self.open_or_create(todos=asdict(self))
        self.printTodos()


    def complete(self, task_id):

        temp = self.open_or_create()

        if os.path.exists(data_path):

            for todo in temp:
                if int(todo['id']) == task_id:
                    todo['done'] = True
                    todo['done_at'] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

            with open(data_path, 'r+') as todos:
                todos.seek(0)
                todos.truncate()

                json.dump(temp, todos, indent=4)

        self.printTodos()


    def delete(self, task_id):
        
        temp = self.open_or_create()

        if os.path.exists(data_path):

            for todo in temp:
                if int(todo['id']) == task_id:
                    del temp[temp.index(todo)]

            with open(data_path, 'r+') as todos:
                todos.seek(0)
                todos.truncate()

                json.dump(temp, todos, indent=4)

        self.printTodos()


    def reset(self, task_id):

        temp = self.open_or_create()

        if os.path.exists(data_path):

            for todo in temp:
                if int(todo['id']) == task_id:
                    todo['done'] = False
                    todo['done_at'] = ''

            with open(data_path, 'r+') as todos:
                todos.seek(0)
                todos.truncate()

                json.dump(temp, todos, indent=4)

        self.printTodos()


    def reset_all(self):

        temp = self.open_or_create()

        for todo in temp:
            todo['done_at'] = ''
            todo['done'] = False

        with open(data_path, 'r+') as todos:
            todos.seek(0)
            todos.truncate()

            json.dump(temp, todos, indent=4)

        self.printTodos()


    def delete_all(self):

        with open(data_path, 'r+') as todos:
            todos.truncate(0)

        self.printTodos()


    def complete_all(self):

        temp = self.open_or_create()

        if os.path.exists(data_path):

            for todo in temp:
                todo['done'] = True
                todo['done_at'] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

            with open(data_path, 'r+') as todos:
                todos.seek(0)
                todos.truncate()

                json.dump(temp, todos, indent=4)
        
        self.printTodos()

from dataclasses import dataclass, asdict
from typing import Any, Literal
from datetime import datetime
from colorama import Fore
import pretty_tables
import json
import os



# Task class
@dataclass(frozen=False, order=True)
class Task:
    id: int = 1
    name: str = ''
    done: bool = False
    created_at: str = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    done_at: str = ''
    data_path = f'{os.getcwd()}/data/.todos.json'



    def open(self, todos = None) -> (Any | Literal[False] | None):

        if todos is None:
            if os.path.exists(self.data_path):
                with open(self.data_path, 'r') as todos:
                    tasks = json.load(todos)
                    return tasks

        else:
            if not os.path.exists(self.data_path):

                with open(self.data_path, 'w+') as todos:

                    task = [asdict(self)]
                    json.dump(task, todos, indent=4)

            elif os.path.exists(self.data_path):

                with open(self.data_path, 'r+') as todos:
                    
                    tasks = json.load(todos)

                    self.id = tasks[-1]['id'] + 1
                    tasks.append(asdict(self))
                    todos.seek(0)
                    todos.truncate()
                    json.dump(tasks, todos, indent=4)

    def printTodos(self):
        """Read your todo's and display it to the CLI
        """
        headers = ["Nº", "Name", "Done?", "Created at", "Completed at"]
        rows = []
        total_pending = 0

        for todo in self.open():

            if not todo['done']:
                todo['done'] = ' No'
                total_pending += 1 
            else:
                todo['done'] = " \u2705"

            if not todo['done_at']:
                todo['done_at'] = 'Not completed yet.'

            rows.append([todo['id'], todo['name'], todo['done'], todo['created_at'], todo['done_at']])

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
        self.open(todos=asdict(self))


    def complete(self, task_id):

        temp = self.open()

        if not os.path.exists(self.data_path):

            print(Fore.RED + "Error" + Fore.RESET +" - You don't have tasks yet. Add one using the -a or -add followed by the name of the task.")

        elif os.path.exists(self.data_path):

            for todo in temp:
                if int(todo['id']) == task_id:
                    todo['done'] = True
                    todo['done_at'] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

            with open(self.data_path, 'r+') as todos:
                todos.seek(0)
                todos.truncate()

                json.dump(temp, todos, indent=4)


    def delete(self, task_id):
        
        temp = self.open()

        if not os.path.exists(self.data_path):

            print(Fore.RED + "Error" + Fore.RESET +" - You don't have tasks yet. Add one using the -a or -add followed by the name of the task.")

        elif os.path.exists(self.data_path):

            for todo in temp:
                if int(todo['id']) == task_id:
                    del temp[temp.index(todo)]

            with open(self.data_path, 'r+') as todos:
                todos.seek(0)
                todos.truncate()

                json.dump(temp, todos, indent=4)
        

###### Use for testing.
# Task(5, 'a', False, datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), '').add()
# Task().printTodos()
# Task().complete(5)
# Task().delete(5)


# win - USER PATH - FUTURE IDEA FOR LAUNCH
# print(os.path.expanduser('~/documents/'))
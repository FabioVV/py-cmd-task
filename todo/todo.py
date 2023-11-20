from dataclasses import dataclass, asdict
from typing import Any, Literal
from datetime import datetime
from colorama import Fore
import pretty_tables
import json
import os

# Main 'Database' file
data_path = f'{os.getcwd()}/data/.todos.json'



# Task class
@dataclass(frozen=False, order=True)
class Task:
    id: int
    name: str
    done: bool
    created_at: str
    done_at: str

    def __init__(self):
        self.created_at = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.done_at = ''
        

    def open(self, todos = None) -> (Any | Literal[False] | None):

        if todos is None:
            if os.path.exists(data_path):
                with open(f'{os.getcwd()}/data/.todos.json', 'r') as todos:
                    tasks = json.load(todos)
                    return tasks

            else: return False

        else:
            if not os.path.exists(data_path):

                with open(f'{os.getcwd()}/data/.todos.json', 'w+') as todos:

                    task = [asdict(self)]
                    json.dump(task, todos, indent=4)
                     


            elif os.path.exists(data_path):

                with open(f'{os.getcwd()}/data/.todos.json', 'r+') as todos:
                    
                    tasks = json.load(todos)
                    tasks.append(asdict(self))
                    todos.seek(0)
                    todos.truncate()
                    json.dump(tasks, todos, indent=4)

            else:
                return False




    def printTodos(self):
        """Read your todo's and display it to the CLI
        """
        headers = ["Nº", "Name", "Done?", "Created at", "Completed at"]
        rows = []
        total_pending = 0

        for todo in self.open():

            if not todo['done']:
                todo['done'] = 'No'
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
        print(Fore.WHITE + f'| Total tasks pending... > {str(total_pending)} {" "*36} |')
        print(Fore.RED + '-'*67)

        for _ in range(2):
            print(Fore.RESET + '')


    def add(self):
        """Add todo's to your list
        """
        self.open(todos=asdict(self))


    def complete(self):
        pass

    def delete(self):
        pass




 # Used for testing.
Task().printTodos()
from dataclasses import dataclass, asdict
from datetime import datetime
import json
import os
from typing import Any, Literal


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

    # Don't need this. Not right now. Maybe never.
    # def __init__(self, id, name, done, created_at, done_at):
    #     self.id = id
    #     self.name = name
    #     self.done = done
    #     self.created_at = created_at
    #     self.done_at = done_at


    def open(self, todos = None) -> (Any | Literal[False] | None):

        print(todos)

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
        pass

    def countPending(self):
        pass

    def add(self):
        """Add todo's to your list
        """
        self.open(todos=asdict(self))
        

    def complete(self):
        pass

    def delete(self):
        pass




 # Used for testing.
Task(2,'testes', False, datetime.today().strftime("%Y-%m-%d %H:%M:%S"), datetime.today().strftime("%Y-%m-%d %H:%M:%S")).add()
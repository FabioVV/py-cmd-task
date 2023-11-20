from dataclasses import dataclass, asdict
from datetime import datetime
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
    created_at: datetime
    done_at: datetime

    # Don't need this. Not right now. Maybe never.

    # def __init__(self, id, name, done, created_at, done_at):
    #     self.id = id
    #     self.name = name
    #     self.done = done
    #     self.created_at = created_at
    #     self.done_at = done_at


    def open(self, todos) -> None:
        if os.path.exists(data_path):
            with open(f'{os.getcwd()}/data/.todos.json', 'r+') as todo:
                self.created_at = json.dumps(self.created_at.strftime("%Y-%m-%d %H:%M:%S")) 
                self.done_at = json.dumps(self.done_at.strftime("%Y-%m-%d %H:%M:%S")) 
                tasks = json.load(todo)
                tasks.append(asdict(self))

                todo.seek(0)
                todo.truncate()
                json.dump(tasks, todo, indent=4)

        else: return False



    def printTodos(self):
        pass

    def countPending(self):
        pass

    def add(self):
        """Add todo's to your list
        """

        if not self.open(todos=asdict(self)):
            with open(f'{os.getcwd()}/data/.todos.json', 'a+') as todo:

                self.created_at = json.dumps(self.created_at.strftime("%Y-%m-%d %H:%M:%S")) 
                self.done_at = json.dumps(self.done_at.strftime("%Y-%m-%d %H:%M:%S")) 
                task = [asdict(self)]
                json.dump(task, todo, indent=4)

    def complete(self):
        pass

    def delete(self):
        pass




 # Used for testing.
Task(2,'testes', False, datetime.today(), datetime.today()).add()
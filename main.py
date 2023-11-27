from todo.todo import Task
import subprocess
import platform
import argparse
import sys
import os

# Initialize main variables - (I may not be using them right now.)
parser = argparse.ArgumentParser(description='Todo CLI.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-l', '--list', help='Write this if you want to list your tasks.', action="store_true")
parser.add_argument('-d', '--delete', help='Write this if you want to delete a task. Should be followed either by the name of the task, or its corresponding number.')
parser.add_argument('-a', '--add', help='Write this if you want to add a task to your list.')
parser.add_argument('-c', '--complete', help='Write this if you want to complete a task. Should be followed by its corresponding number.')

args = parser.parse_args()
config = vars(args)

def main():

  # Check to see if any number of arguments have been passed
  if not len(sys.argv) > 1:
    match platform.system():

      case 'Windows':
        subprocess.call('cls', shell=True)
        subprocess.call(f'python {os.path.basename(__file__)} -h', shell=True)
        subprocess.call('echo Hello, friend.', shell=True)
      case _:
        subprocess.call('clear', shell=True)
        subprocess.call(f'python3 {os.path.basename(__file__)} -h', shell=True)
        subprocess.call('echo Hello, friend.', shell=True)

  else:
    match platform.system():
      
      case 'Windows':
        subprocess.call('cls', shell=True)
      case _:
        subprocess.call('clear', shell=True)


    if args.list:
      Task().printTodos()

    elif args.add:
      Task(name=str(args.add)).add()
      Task().printTodos()

    elif args.complete:
      try:
        Task().complete(int(args.complete))
      except Exception:
        print('Please, enter a number corresponding to a task.')
      finally:
        Task().printTodos()


    elif args.delete:
      try:
        Task().delete(int(args.delete))
      except Exception:
        print('Please, enter a number corresponding to a task.')
      finally:
        Task().printTodos()

if __name__ == '__main__':
  main()
from utils.my_utilities import print_success_plus_warning, print_success, print_error, print_two_spaces
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from json import JSONDecodeError
from subprocess import call
from platform import system
from todo.todo import Task
from colorama import Fore
from sys import argv
from os import path



# Initialize main variables
parser = ArgumentParser(description='Todo CLI.', formatter_class=ArgumentDefaultsHelpFormatter)

parser.add_argument('-a', '--add', help='Write this if you want to add a task to your list.')
parser.add_argument('-l', '--list', help='Write this if you want to list your tasks.', action="store_true")
parser.add_argument('-d', '--delete', help='Write this if you want to delete a task. Should be followed either by the name of the task, or its corresponding number.')
parser.add_argument('-c', '--complete', help='Write this if you want to complete a task. Should be followed by its corresponding number.')
parser.add_argument('-r', '--reset', help='Write this if you want to reset one of your tasks. Reseting will mark the task as uncompleted. THIS ACTION IS IRREVERSIBLE.')
parser.add_argument('-dall', '--delete_all', help='Write this if you want to delete all your tasks. THIS ACTION IS IRREVERSIBLE.', action="store_true")
parser.add_argument('-rall', '--reset_all', help='Write this if you want to reset all your tasks. Reseting will mark all tasks as uncompleted. THIS ACTION IS IRREVERSIBLE.', action="store_true")
parser.add_argument('-call', '--complete_all', help='Write this if you want to complete all your tasks. THIS ACTION IS IRREVERSIBLE.', action="store_true")

args = parser.parse_args()
config = vars(args)

def main():

  # Check to see if any number of arguments have been passed
  if not len(argv) > 1:
    match system():

      case 'Windows':
        call('cls', shell=True)
        call(f'python {path.basename(__file__)} -h', shell=True)
        call('echo Hello, friend.', shell=True)
      case _:
        call('clear', shell=True)
        call(f'python3 {path.basename(__file__)} -h', shell=True)
        call('echo Hello, friend.', shell=True)

  else:
    match system():
      
      case 'Windows':
        call('cls', shell=True)
      case _:
        call('clear', shell=True)


    if args.list:
      Task().printTodos()


    elif args.add:
      Task(name=str(args.add)).add()
      print_success(success=f'added new task named ' + Fore.CYAN + f'{str(args.add)}')


    elif args.complete:
      try:
        Task().complete(int(args.complete))
        print_success(success=f'your task number {str(args.complete)} has been marked as completed.')

      except ValueError:
        print_error(error='please, enter a number corresponding to a task.')


    elif args.delete:
      try:
        Task().delete(int(args.delete))
        print_success(success=f'your task number {str(args.delete)} has been deleted.')

      except ValueError:
        print_error(error='unknow option. Run the script again without any arguments to see available commands.')


    elif args.reset:
        try:
          Task().reset(int(args.reset))
          print_success(success=f'your task number {str(args.reset)} has been marked as undone.')

        except Exception:
          print_error(error='unknow option. Run the script again without any arguments to see available commands.')


    elif args.reset_all:
        try:
          Task().reset_all()
          print_success_plus_warning(success='all of your current tasks have been marked as undone.')

        except Exception:
          print_error(error='program was unable to mark all tasks as undone.')


    elif args.delete_all:
        try:
          Task().delete_all()
          print_success_plus_warning(success='all of your tasks have been deleted.')

        except Exception:
          print_error(error='program was unable to delete your tasks.')


    elif args.complete_all:
        try:
          Task().complete_all()
          print_success_plus_warning(success='all of your tasks have been completed.')

        except JSONDecodeError:
          print_error(error='no tasks found. Use the argument -l to list any tasks you might have.')



if __name__ == '__main__':
  main()
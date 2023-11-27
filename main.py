from utils.my_utilities import print_two_spaces
from json import JSONDecodeError
from todo.todo import Task
from colorama import Fore
from subprocess import call
from platform import system
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys
import os



# Initialize main variables - (I may not be using them right now.)
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
  if not len(sys.argv) > 1:
    match system():

      case 'Windows':
        call('cls', shell=True)
        call(f'python {os.path.basename(__file__)} -h', shell=True)
        call('echo Hello, friend.', shell=True)
      case _:
        call('clear', shell=True)
        call(f'python3 {os.path.basename(__file__)} -h', shell=True)
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
      Task().printTodos()
      print(Fore.GREEN + 'Success' + Fore.RESET + ' - added new task named ' + Fore.CYAN + f'{str(args.add)}')
      print(Fore.RESET + '')
      print('')

    elif args.complete:
      try:
        Task().complete(int(args.complete))
        Task().printTodos()
        print(Fore.GREEN + 'Success' + Fore.RESET + f' - your task number {int(args.complete)} has been marked as completed.')
        print_two_spaces()
        

      except ValueError:
        print(Fore.RED + 'Error' + Fore.RESET +' - Please, enter a number corresponding to a task.')


    elif args.delete:
      try:
        Task().delete(int(args.delete))
        Task().printTodos()
        print(Fore.GREEN + 'Success' + Fore.RESET + f' - your task number {int(args.delete)} has been deleted.')
        print_two_spaces()

      except ValueError:
        print_two_spaces()
        print(Fore.RED + 'Error' + Fore.RESET +' - Unknow option. Run the script again without any arguments to see available commands.')
        print_two_spaces()

    elif args.reset:
        try:
          Task().reset(int(args.reset))
          Task().printTodos()
          print(Fore.GREEN + 'Success' + Fore.RESET + f' - your task number {int(args.reset)} has been marked as undone.')
          print_two_spaces()

        except Exception:
          print_two_spaces()
          print(Fore.RED + 'Error' + Fore.RESET +' - Unknow option. Run the script again without any arguments to see available commands.')
          print_two_spaces()

    elif args.reset_all:
        try:
          Task().reset_all()
          Task().printTodos()
          print(Fore.RED + 'IRREVERSIBLE' + Fore.RESET +' - this action is irreversible.')
          print(Fore.GREEN + 'Success' + Fore.RESET +' - all of your current tasks have been marked as undone.')
          print_two_spaces()

        except Exception:
          print_two_spaces()
          print(Fore.RED + 'Error' + Fore.RESET +' - program was unable to mark all tasks as undone.')
          print_two_spaces()
        
    elif args.delete_all:
        try:
          Task().delete_all()
          Task().printTodos()
          print(Fore.RED + 'IRREVERSIBLE' + Fore.RESET +' - this action is irreversible.')
          print(Fore.GREEN + 'Success' + Fore.RESET +' - all of your tasks have been deleted.')
          print_two_spaces()

        except Exception:
          print_two_spaces()
          print(Fore.RED + 'Error' + Fore.RESET +' - program was unable to delete your tasks.')
          print_two_spaces()

    elif args.complete_all:
        try:
          Task().complete_all()
          Task().printTodos()
          print(Fore.RED + 'IRREVERSIBLE' + Fore.RESET +' - this action is irreversible.')
          print(Fore.GREEN + 'Success' + Fore.RESET +' - all of your tasks have been completed.')
          print_two_spaces()

        except JSONDecodeError:
          print_two_spaces()
          print(Fore.RED + 'Error' + Fore.RESET +' - No tasks found. Use the argument -l to list any tasks you might have.')
          print_two_spaces()


if __name__ == '__main__':
  main()
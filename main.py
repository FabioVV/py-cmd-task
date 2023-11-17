from prettytable import PrettyTable
from todo import todo
import subprocess
import platform
import json
import os

# Initialize main variables - (I may not be using them right now.)
commands = ['']


def main():

  match platform.system():
    case 'Windows':
      subprocess.call('cls', shell=True)
    case _:
      subprocess.call('clear', shell=True)


  subprocess.call('echo Hello, friend.', shell=True)





  table = PrettyTable()
  



 
if __name__ == '__main__':
  main()
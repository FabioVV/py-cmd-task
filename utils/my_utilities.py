from colorama import Fore

# Function for spacing - ?????? Don't ask me whatever this is.
def print_two_spaces():
  """The name.
  """
  
  print()
  print()



def print_success_plus_warning(warning: str = 'this action is irreversible.', success: str = ''):
    """
    Prints a generic or custom warning message with a success message. 
    Spaces should be handle by the 'print_two_spaces' function, in the utils, my_utilities python file.
    """

    print(Fore.RED + 'IRREVERSIBLE' + Fore.RESET + f' - {warning.rstrip().lstrip()}')
    print(Fore.GREEN + 'Success' + Fore.RESET + f' - {success.rstrip().lstrip()}')
    print_two_spaces()

  
def print_error(error: str = 'An error has occured.'):
    """
    Prints a generic or custom error message with spacing below it. 
    """

    print_two_spaces()
    print(Fore.RED + 'Error' + Fore.RESET + f' - {error.rstrip().lstrip()}')
    print_two_spaces()


def print_success(success: str = 'Success.'):
    """
    Prints a generic or success message with spacing below it. 
    """

    print(Fore.GREEN + 'Success' + Fore.RESET + f' - {success.rstrip().lstrip()}')
    print(Fore.RESET + '')
    print_two_spaces()

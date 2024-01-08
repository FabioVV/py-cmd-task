from colorama import Fore



def print_success_plus_warning(warning: str = 'this action is irreversible.', success: str = ''):
    """
    Prints a generic or custom warning message with a success message. 
    """

    print(Fore.RED + 'IRREVERSIBLE' + Fore.RESET + f' - {warning.rstrip().lstrip()}')
    print(Fore.GREEN + 'Success' + Fore.RESET + f' - {success.rstrip().lstrip()}')
    print()
    print()

  
def print_error(error: str = 'An error has occured.'):
    """
    Prints a generic or custom error message with spacing below it. 
    """

    print()
    print(Fore.RED + 'Error' + Fore.RESET + f' - {error.rstrip().lstrip()}')
    print()


def print_success(success: str = 'Success.'):
    """
    Prints a generic or success message with spacing below it. 
    """

    print(Fore.GREEN + 'Success' + Fore.RESET + f' - {success.rstrip().lstrip()}')
    print(Fore.RESET + '')

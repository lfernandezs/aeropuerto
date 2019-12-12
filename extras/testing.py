from termcolor import colored

def print_test(mensaje, condicion):
    if condicion:
        print(mensaje, colored("OK", 'green'))
    else:
        print(mensaje, colored("ERROR", 'red'))

def print_titulo(titulo):
    print(colored(titulo, 'cyan'))
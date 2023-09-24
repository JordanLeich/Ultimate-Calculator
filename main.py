# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors


import calculators.calculators
import conversions.conversions
from modules import extras, colors
from modules.errors import Exit
from gui import start_gui

def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        print(colors.green + '---Ultimate Calculator---', colors.reset)
        print('''Options:
        (1) Calculators
        (2) Converters
        (3) GUI Version
        (4) Extras
        (5) Exit''')

        choice = input('Enter your choice: ')
        print("")

        if choice == '1':
            try:
                calculators.calculators.start()
            except Exit:
                break
        elif choice == '2':
            try:
                conversions.conversions.start()
            except Exit:
                break
        elif choice == '3':
            print(colors.green + 'GUI Application is now running!\n', colors.reset)
            start_gui()
        elif choice == '4':
            extras.start()
        elif choice == '5':
            print('Exiting the Ultimate Calculator...')
            break
        else:
            print(colors.red + "Invalid Choice. Please select a valid option.\n", colors.reset)

if __name__ == '__main__':
    main_menu()

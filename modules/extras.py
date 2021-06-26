import webbrowser
import time
from modules import colors


def contributions():
    """
Allows the user to be able to view all of the contributors of this project via GitHub
    """
    print(colors.green + "Opening all contributors of this project...\n", colors.reset)
    webbrowser.open_new(
        "https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors")
    time.sleep(2)


def releases():
    """
Allows the user to be able to view either the latest or oldest release of this project via GitHub
    """
    while True:
        choice = int(input('''(1) Latest Stable Release
(2) Oldest Release
(3) Return to previous window
(4) Exit

Which release would you like to view: '''))
        print()

        if choice == 1:
            print(colors.green + "Opening the latest stable release...\n", colors.reset)
            time.sleep(1)
            webbrowser.open_new(
                "https://github.com/JordanLeich/Ultimate-Calculator/releases")
            time.sleep(1)
        elif choice == 2:
            print(colors.green + "Opening the oldest release...\n", colors.reset)
            time.sleep(1)
            webbrowser.open_new(
                "https://github.com/JordanLeich/Ultimate-Calculator/releases/tag/v1.0")
            time.sleep(1)
        elif choice == 3:
            return
        elif choice == 4:
            break
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)
    print("Reached end of the program... Ending program...\n")
    exit()


def donate():
    while True:
        print(colors.yellow + 'Since this project is completely free to use and open source, users have the option to '
                              'send a donation of their choice but this action is not required.\n', colors.reset)
        time.sleep(2)
        donate_choice = int(input('''(1) PayPal
(2) Cash App
(3) Return to previous window
(4) Exit
    
Which donation option would you like to use: '''))
        print()

        if donate_choice == 1:
            print(colors.green + "Opening PayPal Donation page...\n", colors.reset)
            webbrowser.open_new(
                "https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")
            time.sleep(2)
        elif donate_choice == 2:
            print(colors.green + "Opening Cash App Donation page...\n", colors.reset)
            webbrowser.open_new(
                "https://cash.app/$JordanLeich")
            time.sleep(2)
        elif donate_choice == 3:
            return
        elif donate_choice == 4:
            break
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)
    print("Reached end of the program... Ending program...\n")
    exit()


def start():
    while True:
        choice = int(input('''(1) Project Releases
(2) Credits
(3) Donate
(4) Return to main window
(5) Exit
    
Which option would you like: '''))
        print()

        if choice == 1:
            releases()
        elif choice == 2:
            contributions()
        elif choice == 3:
            donate()
        elif choice == 4:
            return
        elif choice == 5:
            break
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)
    print("Reached end of the program... Ending program...\n")
    exit()


if __name__ == '__main__':
    start()

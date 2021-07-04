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
            release_opener("Opening the latest stable release...\n",
                           "https://github.com/JordanLeich/Ultimate-Calculator/releases")

        elif choice == 2:
            release_opener("Opening the oldest release...\n",
                           "https://github.com/JordanLeich/Ultimate-Calculator/releases/tag/v1.0")

        elif choice == 3:
            return
        elif choice == 4:
            break
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)
    print("Reached end of the program... Ending program...\n")
    exit()


def release_opener(arg0, arg1):
    print(colors.green + arg0, colors.reset)
    time.sleep(1)
    webbrowser.open_new(arg1)
    time.sleep(1)


def donate():
    """
Allows the user to be able to donate via PayPal or Cash App methods
    """
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
            donation_opener("Opening PayPal Donation page...\n",
                            "https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")

        elif donate_choice == 2:
            donation_opener("Opening Cash App Donation page...\n", "https://cash.app/$JordanLeich")

        elif donate_choice == 3:
            return
        elif donate_choice == 4:
            break
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)
    print("Reached end of the program... Ending program...\n")
    exit()


def donation_opener(arg0, arg1):
    print(colors.green + arg0, colors.reset)
    webbrowser.open_new(arg1)
    time.sleep(2)


def start():
    """
Main hub UI for the user to view additional information or extra parts of this project
    """
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

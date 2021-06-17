import webbrowser
import time
from modules import colors, restart


def start():
    choice = int(input('''(1) Latest Stable Release
(2) Oldest Release

Which release would you like to view: '''))
    print()

    if choice == 1:
        print(colors.green + "Opening the latest stable release...\n", colors.reset)
        time.sleep(1)
        webbrowser.open_new(
            "https://github.com/JordanLeich/Ultimate-Calculator/releases")
        time.sleep(1)
        restart.restart()
    elif choice == 2:
        print(colors.green + "Opening the oldest release...\n", colors.reset)
        time.sleep(1)
        webbrowser.open_new(
            "https://github.com/JordanLeich/Ultimate-Calculator/releases/tag/v1.0")
        time.sleep(1)
        restart.restart()
    else:
        print(colors.red + 'User input error found...\n', colors.reset)
        time.sleep(2)
        restart.restart()


if __name__ == '__main__':
    start()

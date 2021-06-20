import webbrowser
import time
from modules import colors


def start():
    """
Allows the user to be able to view all of the contributors of this project via GitHub
    """
    print(colors.green + "Opening all contributors of this project...\n", colors.reset)
    webbrowser.open_new(
        "https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors")
    time.sleep(2)


if __name__ == '__main__':
    start()

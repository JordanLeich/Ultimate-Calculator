import webbrowser
import time
import colors
import restart


def start():
    print(colors.green + "Opening all contributors of this project...\n", colors.reset)
    time.sleep(1)
    webbrowser.open_new(
        "https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors")
    time.sleep(2)
    restart.restart()


if __name__ == '__main__':
    start()

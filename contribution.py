import webbrowser
import time


def start():
    print("Opening all current contributors of this project...")
    time.sleep(1.5)
    webbrowser.open_new("https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors")
    time.sleep(2)
    quit()

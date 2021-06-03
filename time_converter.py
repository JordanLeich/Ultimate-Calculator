import restart
import colors
import time


def time_convert():
    print("Input what you would like to convert from")
    print("Please stick to this format")
    print(colors.red, "XY XD XH XM XS (X is your number)\t ie: 10Y", colors.reset)

    response = input().split()
    totalseconds = 0
    for date in response:

        if date.endswith("d") or date.endswith("D"):
            date = date[:-1]
            date = float(date)
            date = date * 86400
            totalseconds += date
        elif date.endswith("h") or date.endswith("H"):
            date = date[:-1]
            date = float(date)
            date = date * 3600
            totalseconds += date
        elif date.endswith("m") or date.endswith("M"):
            date = date[:-1]
            date = float(date)
            date = date * 60
            totalseconds += date
        elif date.endswith("s") or date.endswith("S"):
            date = date[:-1]
            date = float(date)
            totalseconds += date
        elif date.endswith("y") or date.endswith("Y"):
            date = date[:-1]
            date = float(date)
            date = date * 31536000
            totalseconds += date

    convert_to = input("""
    What do you want to convert TO?
    (1) Years
    (2) Days
    (3) Minutes
    (4) Seconds
    """)
    convert_to = int(convert_to)
    if convert_to == 1:
        print(colors.green, f"{totalseconds / 31536000} years", colors.reset)
    elif convert_to == 2:
        print(colors.green, f"{totalseconds / 86400} days", colors.reset)
    elif convert_to == 3:
        print(colors.green, f"{totalseconds / 60} minutes", colors.reset)
    elif convert_to == 4:
        print(colors.green, f"{totalseconds} seconds", colors.reset)
    else:
        print(colors.red+"Invalid input... Restarting input...\n"+colors.reset)
        time.sleep(2)
        time_convert()


def start():
    time_convert()
    restart.restart()

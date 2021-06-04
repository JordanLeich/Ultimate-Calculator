import time
import colors
import restart


def time_convert():
    print("Input what you would like to convert from")
    print("Please stick to this format")
    print(colors.red, "XY XD XH XM XS (X is your number)\t ie: 10Y", colors.reset)

    response = input().split()
    total_seconds = 0
    for date in response:

        if date.endswith("d") or date.endswith("D"):
            date = date[:-1]
            date = float(date)
            date *= 86400
            total_seconds += date
        elif date.endswith("h") or date.endswith("H"):
            date = date[:-1]
            date = float(date)
            date *= 3600
            total_seconds += date
        elif date.endswith("m") or date.endswith("M"):
            date = date[:-1]
            date = float(date)
            date *= 60
            total_seconds += date
        elif date.endswith("s") or date.endswith("S"):
            date = date[:-1]
            date = float(date)
            total_seconds += date
        elif date.endswith("y") or date.endswith("Y"):
            date = date[:-1]
            date = float(date)
            date *= 31536000
            total_seconds += date

    convert_to = input("""
    What do you want to convert TO?
    (1) Years
    (2) Days
    (3) Minutes
    (4) Seconds
    """)
    convert_to = int(convert_to)
    if convert_to == 1:
        print(colors.green, f"{total_seconds / 31536000} years", colors.reset)
    elif convert_to == 2:
        print(colors.green, f"{total_seconds / 86400} days", colors.reset)
    elif convert_to == 3:
        print(colors.green, f"{total_seconds / 60} minutes", colors.reset)
    elif convert_to == 4:
        print(colors.green, f"{total_seconds} seconds", colors.reset)
    else:
        print(colors.red + "Invalid input... Restarting input...\n" + colors.reset)
        time.sleep(2)
        time_convert()


def start():
    time_convert()
    restart.restart()

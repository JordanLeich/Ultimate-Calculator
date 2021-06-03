import restart

def start():
    timeconvert()
    restart.restart()

def timeconvert():
    print("""
    Input what you would like to convert FROM
    (Where X is a number, format:
    XY XD XH XM XS
    You don't have to fill in everything""")
    response = input().split()
    totalseconds = 0
    for date in response:
        print
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
        else:
            pass
    convertto = input("""
    What do you want to convert TO?
    (1) Years
    (2) Days
    (3) Minutes
    (4) Seconds

    """)
    convertto = int(convertto)
    if convertto == 1:
        print(f"{totalseconds / 31536000} years")
    elif convertto == 2:
        print(f"{totalseconds / 86400} days")
    elif convertto == 3:
        print(f"{totalseconds / 60} minutes")
    elif convertto == 4:
        print(f"{totalseconds} seconds")

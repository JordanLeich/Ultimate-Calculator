import colors
import end
import restart
import time
from currency_api import get_currency
from tools import repeat_input


def currency_converter():
    user_choice = int(
        input("""(1) US Dollar to ALL
(2) Euro to ALL
(3) Canadian Dollar to ALL
(4) Japanese Yen to ALL
(5) Moroccan MAD to ALL
Select a currency conversion: """))
    print()
    if user_choice == 1:
        user_dollar = float(input("Dollar Amount: "))

        d_to_e = float(user_dollar * get_currency("USD_EUR"))
        d_to_j = float(user_dollar * get_currency("USD_JPY"))
        d_to_c = float(user_dollar * get_currency("USD_CAD"))
        d_to_mad = float(user_dollar * get_currency("USD_MAD"))
        print(colors.green, user_dollar, "in US Dollar equals",
              d_to_e, "in Euros.")
        print(colors.green, user_dollar, "in US Dollar equals",
              d_to_j, "in Japanese Yen.")
        print(colors.green, user_dollar, "in US Dollar equals",
              d_to_c, "in Canadian Dollar.")
        print(colors.green, user_dollar, "in US Dollar equals",
              d_to_mad, "in Moroccan MAD.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        user_euro = float(input("Euro Amount: "))
        print()
        e_to_d = float(user_euro * get_currency("EUR_USD"))
        e_to_j = float(user_euro * get_currency("EUR_JPY"))
        e_to_c = float(user_euro * get_currency("EUR_CAD"))
        e_to_mad = float(user_euro * get_currency("EUR_MAD"))
        print(colors.green, user_euro, "in Euro equals",
              e_to_d, "in US Dollars.")
        print(colors.green, user_euro, "in Euro equals",
              e_to_j, "in Japanese Yen.")
        print(colors.green, user_euro, "in Euro equals",
              e_to_c, "in Canadian Dollar.")
        print(colors.green, user_euro, "in Euro equals",
              e_to_mad, "in Moroccan MAD.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        user_canadian = float(input("Canadian Dollar Amount: "))
        print()
        c_to_d = float(user_canadian * get_currency("CAD_USD"))
        c_to_j = float(user_canadian * get_currency("CAD_JPY"))
        c_to_e = float(user_canadian * get_currency("CAD_EUR"))
        c_to_mad = float(user_canadian * get_currency("CAD_MAD"))
        print(colors.green, user_canadian, "in Canadian Dollar equals",
              c_to_d, "in US Dollars.")
        print(colors.green, user_canadian, "in Canadian Dollar equals",
              c_to_j, "in Japanese Yen.")
        print(colors.green, user_canadian, "in Canadian Dollar equals",
              c_to_e, "in Euro.")
        print(colors.green, user_canadian, "in Canadian Dollar equals",
              c_to_mad, "in Moroccan MAD.\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        user_yen = float(input("Japanese Yen Amount: "))
        print()
        y_to_d = float(user_yen * get_currency("JPY_USD"))
        y_to_e = float(user_yen * get_currency("JPY_EUR"))
        y_to_c = float(user_yen * get_currency("JPY_CAD"))
        y_to_mad = float(user_yen * get_currency("JPY_MAD"))
        print(colors.green, user_yen, "in Japanese Yen equals",
              y_to_d, "in US Dollars.")
        print(colors.green, user_yen, "in Japanese Yen equals",
              y_to_e, "in Euros.")
        print(colors.green, user_yen, "in Japanese Yen equals",
              y_to_c, "in Canadian Dollar.")
        print(colors.green, user_yen, "in Japanese Yen equals",
              y_to_mad, "in Moroccan MAD.\n")
        restart.restart()
    elif user_choice == 5:
        user_mad = float(input("Moroccan MAD Amount: "))
        print()
        mad_to_d = float(user_mad * get_currency("MAD_USD"))
        mad_to_e = float(user_mad * get_currency("MAD_EUR"))
        mad_to_c = float(user_mad * get_currency("MAD_CAD"))
        mad_to_yen = float(user_mad * get_currency("MAD_JPY"))
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_d, "in US Dollars.")
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_e, "in Euros.")
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_c, "in Canadian Dollar.")
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_yen, "in Japanese Yen.\n", colors.reset)
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        currency_converter()


# Temperatures
def celsius_to_all(data):
    data = float(data)
    fahrenheit = data * 1.8 + 32
    kelvin = data + 273.15

    return fahrenheit, kelvin


def fahrenheit_to_all(data):
    data = float(data)
    celsius = (data - 32) * 5 / 9
    kelvin = (data - 32) * 5 / 9 + 273.15

    return celsius, kelvin


def kelvin_to_all(data):
    data = float(data)
    celsius = data - 273.15
    fahrenheit = (data - 273.15) * 1.8 + 32

    return celsius, fahrenheit


def temp_converter():
    """
    Handles all temperature conversions here
    """
    user_choice = int(
        input("""
(1) Celsius to ALL
(2) Fahrenheit to ALL
(3) Kelvin to ALL
Select a temperature conversion: """))
    print()

    if user_choice == 1:
        user_celsius = repeat_input("Celsius: ", "Invalid Number...\n", "float")
        print()

        fahrenheit, kelvin = celsius_to_all(user_celsius)
        print(f"{colors.green}{user_celsius} Celsius is {fahrenheit} in Fahrenheit.")
        print(f"{colors.green}{user_celsius} Celsius is {kelvin} in Kelvin. {colors.reset}\n")
        restart.restart()
    elif user_choice == 2:
        user_fahrenheit = repeat_input("Fahrenheit: ", "Invalid Number...\n", "float")
        print()

        celsius, kelvin = fahrenheit_to_all(user_fahrenheit)
        print(f"{colors.green}{user_fahrenheit} Fahrenheit is {celsius} in Celsius.")
        print(f"{colors.green}{user_fahrenheit} Fahrenheit is {kelvin} in Kelvin. {colors.reset}\n")
        restart.restart()
    elif user_choice == 3:
        user_kelvin = repeat_input("Kelvin: ", "Invalid Number...\n", "float")
        print()

        celsius, fahrenheit = kelvin_to_all(user_kelvin)
        print(f"{colors.green}{user_kelvin} Kelvin is {celsius} in Celsius.")
        print(f"{colors.green}{user_kelvin} Kelvin is {fahrenheit} in Fahrenheit. {colors.reset}\n")
        restart.restart()
    else:
        print(f"{colors.red}Invalid input... Restarting input choice... {colors.reset}\n")
        time.sleep(2)
        temp_converter()


# Masses
def kilograms_to_all(data):
    data = float(data)

    grams = data * 1000
    pounds = data * 2.205
    ounces = data * 35.274

    return grams, pounds, ounces


def grams_to_all(data):
    data = float(data)

    kilograms = data / 1000
    pounds = data / 454
    ounces = data / 28.35

    return kilograms, pounds, ounces


def pounds_to_all(data):
    data = float(data)

    kilograms = data / 2.205
    grams = data * 454
    ounces = data * 16

    return kilograms, grams, ounces


def ounces_to_all(data):
    data = float(data)

    kilograms = data / 35.274
    grams = data * 28.35
    pounds = data / 16

    return kilograms, grams, pounds


def mass_converter():
    """
    Handles all mass conversions
    """
    user_choice = int(
        input("""(1) Kilogram to ALL
(2) Grams to ALL
(3) Pounds to ALL
(4) Ounces to ALL
Select a mass conversion: """))
    print()

    if user_choice == 1:
        user_kilo = repeat_input("Kilograms: ", "Invalid Number...\n", "float")
        print()

        grams, pounds, ounces = kilograms_to_all(user_kilo)
        print(f'{colors.green}{user_kilo} Kilograms is {grams} in Grams')
        print(f'{user_kilo} Kilograms is {pounds} in Pounds')
        print(f'{user_kilo} Kilograms is {ounces} in Ounces{colors.reset}\n')
        restart.restart()
    elif user_choice == 2:
        user_gram = repeat_input("Grams: ", "Invalid Number...\n", "float")
        print()

        kilograms, pounds, ounces = grams_to_all(user_gram)
        print(f'{colors.green}{user_gram} Grams is {kilograms} in Kilograms')
        print(f'{user_gram} Grams is {pounds} in Pounds')
        print(f'{user_gram} Grams is {ounces} in Ounces{colors.reset}\n')
        restart.restart()
    elif user_choice == 3:
        user_pound = repeat_input("Pounds: ", "Invalid Number...\n", 'float')
        print()

        kilograms, grams, ounces = pounds_to_all(user_pound)
        print(f'{colors.green}{user_pound} Grams is {kilograms} in Kilograms')
        print(f'{user_pound} Grams is {grams} in Grams')
        print(f'{user_pound} Grams is {ounces} in Ounces{colors.reset}\n')
        restart.restart()
    elif user_choice == 4:
        user_ounce = repeat_input("Ounces: ", "Invalid Number...\n", 'float')
        print()

        kilograms, grams, pounds = ounces_to_all(user_ounce)
        print(f'{colors.green}{user_ounce} Grams is {kilograms} in Kilograms')
        print(f'{user_ounce} Grams is {grams} in Grams')
        print(f'{user_ounce} Grams is {pounds} in Pounds{colors.reset}\n')
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        mass_converter()


# Lengths
def feet_to_all(data):
    data = float(data)

    inch = data * 12
    yard = data / 3
    mile = data / 5280

    return inch, yard, mile


def inches_to_all(data):
    data = float(data)

    feet = data / 12
    yard = data / 36
    mile = data / 63360

    return feet, yard, mile


def yards_to_all(data):
    data = float(data)

    feet = data * 3
    inch = data * 36
    mile = data / 1760

    return feet, inch, mile


def miles_to_all(data):
    data = float(data)

    feet = data * 5280
    inch = data * 63360
    yard = data * 1760

    return feet, inch, yard


def length_converter():
    """
    Handles all length conversions
    """
    user_choice = int(
        input("""(1) Feet to ALL
(2) Inch to ALL
(3) Yard to ALL
(4) Mile to ALL
Select a length conversion: """))
    print()

    if user_choice == 1:
        feet = repeat_input("Feet: ", "Invalid Number...\n", "float")
        print()

        inch, yard, mile = feet_to_all(feet)

        print(f'{colors.green}{feet} in Feet equals {inch} in Inches.')
        print(f'{colors.green}{feet} in Feet equals {yard} in Yards.')
        print(f'{colors.green}{feet} in Feet equals {mile} in Miles.{colors.reset}\n')
        restart.restart()

    elif user_choice == 2:
        inch = repeat_input("Inches: ", "Invalid Number...\n", "float")
        print()

        feet, yard, mile = inches_to_all(inch)
        print(f'{colors.green}{inch} in Inches equals {feet} in Feet.')
        print(f'{colors.green}{inch} in Inches equals {yard} in Yards.')
        print(f'{colors.green}{inch} in Inches equals {mile} in Miles.{colors.reset}\n')
        restart.restart()

    elif user_choice == 3:
        yard = repeat_input("Yards: ", "Invalid Number...\n", "float")
        print()

        feet, inch, mile = yards_to_all(yard)
        print(f'{colors.green}{yard} in Yards equals {feet} in Feet.')
        print(f'{colors.green}{yard} in Yards equals {inch} in Inches.')
        print(f'{colors.green}{yard} in Yards equals {mile} in Miles.{colors.reset}\n')
        restart.restart()

    elif user_choice == 4:
        mile = float(input("Miles: "))
        print()

        feet, inch, yard = miles_to_all(mile)
        print(f'{colors.green}{mile} in Miles equals {feet} in Feet.')
        print(f'{colors.green}{mile} in Miles equals {inch} in Inches.')
        print(f'{colors.green}{mile} in Miles equals {yard} in Yards.{colors.reset}\n')
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        length_converter()


# Volumes
def milliliters_to_liters(data):
    data = float(data)
    return data * (1 / 1000)


def liters_to_milliliters(data):
    data = float(data)
    return data * (1000 / 1)


def gallons_to_all(data):
    data = float(data)

    quart = data * 4
    pint = data * 8
    ounce = data * 128

    return quart, pint, ounce


def quarts_to_all(data):
    data = float(data)

    gallon = data / 4
    pint = data * 2
    ounce = data * 32

    return gallon, pint, ounce


def pints_to_all(data):
    data = float(data)

    gallon = data / 8
    quart = data / 2
    ounce = data * 16

    return gallon, quart, ounce


def ounces_to_all2(data):
    data = float(data)

    gallon = data / 128
    quart = data / 32
    pint = data / 16

    return gallon, quart, pint


def volume_converter():
    """
    Handles all volume conversions
    """
    user_choice = int(
        input("""(1) Milliliters to Liters
(2) Liters to Milliliters
(3) Gallons to ALL
(4) Quarts to ALL
(5) Pints to ALL
(6) Ounces to ALL
Select a volume conversion: """))
    print()

    if user_choice == 1:
        milliliters = repeat_input("Milliliters: ", "Invalid Number...\n", "float")
        print()

        liters = milliliters_to_liters(milliliters)
        print(f'{colors.green}{milliliters} in Milliliters equals {liters} in Liters. {colors.reset}\n')
        restart.restart()

    elif user_choice == 2:
        liters = repeat_input("Liters: ", "Invalid Number...\n", "float")
        print()

        milliliters = liters_to_milliliters(liters)
        print(f'{colors.green}{liters} in Liters equals {milliliters}in Milliliters. {colors.reset}\n')
        restart.restart()

    elif user_choice == 3:
        gallon = repeat_input("Gallons: ", "Invalid Number...\n", "float")
        print()

        quart, pint, ounce = gallons_to_all(gallon)
        print(f'{colors.green}{gallon} in Gallons equals {quart} in Quarts.')
        print(f'{colors.green}{gallon} in Gallons equals {pint} in Pints.')
        print(f'{colors.green}{gallon} in Gallons equals {ounce} in Ounces. {colors.reset}\n')
        restart.restart()

    elif user_choice == 4:
        quart = repeat_input("Quarts: ", "Invalid Number...\n", "float")
        print()

        gallon, pint, ounce = quarts_to_all(quart)
        print(f'{colors.green}{quart} in Quarts equals {gallon} in Gallons.')
        print(f'{colors.green}{quart} in Quarts equals {pint} in Pints.')
        print(f'{colors.green}{quart} in Quarts equals {ounce} in Ounces. {colors.reset}\n')
        restart.restart()

    elif user_choice == 5:
        pint = repeat_input("Pints: ", "Invalid Number...\n", "float")
        print()

        gallon, quart, ounce = pints_to_all(pint)
        print(f'{colors.green}{pint} in Pints equals {gallon} in Gallons.')
        print(f'{colors.green}{pint} in Pints equals {quart} in Quarts.')
        print(f'{colors.green}{pint} in Pints equals {ounce} in Ounces. {colors.reset}\n')
        restart.restart()

    elif user_choice == 6:
        ounce = repeat_input("Ounces: ", "Invalid Number...\n", "float")
        print()

        gallon, quart, pint = ounces_to_all2(ounce)
        print(f'{colors.green}{ounce} in Ounces equals {gallon} in Gallons.')
        print(f'{colors.green}{ounce} in Ounces equals {quart} in Quarts.')
        print(f'{colors.green}{ounce} in Ounces equals {pint} in Pints. {colors.reset}\n')
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        volume_converter()


def crypto_converter():
    """
    Handles all crypto conversion
    """
    user_choice = int(
        input("""(1) Bitcoin to ALL
(2) Ethereum to ALL
(3) DogeCoin  to ALL
(4) SHIBA INU to ALL
Select a crypto conversion:    """))
    print()
    if user_choice == 1:
        btc = float(input("Bitcoin Amount: "))
        print()
        btc_to_e = float(btc * 13.72)
        btc_to_dc = float(btc * 95317.32)
        btc_to_sh = float(btc * 4.03)
        print(colors.green, btc, "in Bitcoin equals",
              btc_to_e, "in Ethereum.")
        print(colors.green, btc, "in Bitcoin equals",
              btc_to_dc, "in DogeCoin.")
        print(colors.green, btc, "in Bitcoin equals",
              btc_to_sh, "B in SHIB INU.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        eth = float(input("Ethereum Amount: "))
        print()
        e_to_b = float(eth * 0.072)
        e_to_dc = float(eth * 6686.2)
        e_to_sh = float(eth * 292.12)
        print(colors.green, eth, "in Ethereum equals",
              e_to_b, "in Bitcoin.")
        print(colors.green, eth, "in Ethereum equals",
              e_to_dc, "in DogeCoin.")
        print(colors.green, eth, "in Euro equals",
              e_to_sh, "M in SHIBA INU.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        doge_c = float(input("DogeCoin Amount: "))
        print()
        dc_to_b = float(doge_c * 0.00001089)
        dc_to_e = float(doge_c * 0.000150)
        dc_to_sh = float(doge_c * 43745)
        print(colors.green, doge_c, "in DogeCoin equals",
              dc_to_b, "in Bitcoin.")
        print(colors.green, doge_c, "in DogeCoin equals",
              dc_to_e, "in Ethereum.")
        print(colors.green, doge_c, "in DogeCoin equals",
              dc_to_sh, "in SHIBA INU.\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        sh = float(input("SHIBA INU Amount: "))
        print()
        sh_to_b = float(sh * 0.00000001)
        sh_to_e = float(sh * 0.0000000012)
        sh_to_dc = float(sh * 0.000023)
        print(colors.green, sh, "in SHIBA INU equals",
              sh_to_b, "in Bitcoin.")
        print(colors.green, sh, "in SHIBA INU equals",
              sh_to_e, "in Ethereum.")
        print(colors.green, sh, "in SHIBA INU equals",
              sh_to_dc, "in DogeCoin.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        crypto_converter()


def mph():
    choice = float(input('How many Miles Per Hour: '))
    print()
    mph_fps = choice * 1.467
    mph_mps = choice / 2.237
    mph_kms = choice * 1.609
    mph_knot = choice / 1.151
    print(colors.green, choice, 'Miles Per Hour equals',
          mph_fps, 'in Foot Per Seconds.')
    print(colors.green, choice, 'Miles Per Hour equals',
          mph_mps, 'in Meters Per Second.')
    print(colors.green, choice, 'Miles Per Hour equals',
          mph_kms, 'in Kilometers Per Hour.')
    print(colors.green, choice, 'Miles Per Hour equals',
          mph_knot, 'in Knot.\n', colors.reset)
    restart.restart()


def fps():
    choice = float(input('How many Foot Per Seconds: '))
    print()
    fps_mph = choice / 1.467
    fps_mps = choice / 3.281
    fps_kph = choice * 1.097
    fps_knot = choice / 1.688
    print(colors.green, choice, 'Foot Per Seconds equals',
          fps_mph, 'in Miles Per Hour.')
    print(colors.green, choice, 'Foot Per Seconds equals',
          fps_mps, 'in Meters Per Second.')
    print(colors.green, choice, 'Foot Per Seconds equals',
          fps_kph, 'in Kilometers Per Hour.')
    print(colors.green, choice, 'Foot Per Seconds equals',
          fps_knot, 'in Knot.\n', colors.reset)
    restart.restart()


def mps():
    choice = float(input('How many Meters Per Second: '))
    print()
    mps_mph = choice * 2.237
    mps_fps = choice * 3.281
    mps_kph = choice * 3.6
    mps_knot = choice * 1.944
    print(colors.green, choice, 'Meters Per Second equals',
          mps_mph, 'in Miles Per Hour.')
    print(colors.green, choice, 'Meters Per Second equals',
          mps_fps, 'in Foot Per Second.')
    print(colors.green, choice, 'Meters Per Second equals',
          mps_kph, 'in Kilometers Per Hour.')
    print(colors.green, choice, 'Meters Per Second equals',
          mps_knot, 'in Knot.\n', colors.reset)
    restart.restart()


def kph():
    choice = float(input('How many Kilometers Per Hour: '))
    print()
    kph_mph = choice / 1.609
    kph_fps = choice / 1.097
    kph_mps = choice / 3.6
    kph_knot = choice / 1.852
    print(colors.green, choice, 'Meters Per Second equals',
          kph_mph, 'in Miles Per Hour.')
    print(colors.green, choice, 'Meters Per Second equals',
          kph_fps, 'in Foot Per Second.')
    print(colors.green, choice, 'Meters Per Second equals',
          kph_mps, 'in Meters Per Second.')
    print(colors.green, choice, 'Meters Per Second equals',
          kph_knot, 'in Knot.\n', colors.reset)
    restart.restart()


def knot():
    choice = float(input('How many Knots: '))
    print()
    knot_mph = choice * 1.151
    knot_fps = choice * 1.688
    knot_mps = choice / 1.944
    knot_kph = choice * 1.852
    print(colors.green, choice, 'Knots equals',
          knot_mph, 'in Miles Per Hour.')
    print(colors.green, choice, 'Knots equals',
          knot_fps, 'in Foot Per Second.')
    print(colors.green, choice, 'Knots equals', knot_mps,
          'in Meters Per Second.')
    print(colors.green, choice, 'Knots equals', knot_kph,
          'in Kilometers Per Hour.\n', colors.reset)
    restart.restart()


def speed_converter():
    choice = int(input("""(1) Miles Per Hour to All
(2) Foot Per Second to ALL
(3) Meter Per Second to ALL
(4) Kilometer Per Hour to ALL
(5) Knot to ALL
Which calculation would you like to perform: """))
    print()

    if choice == 1:
        mph()
    elif choice == 2:
        fps()
    elif choice == 3:
        mps()
    elif choice == 4:
        kph()
    elif choice == 5:
        knot()
    else:
        print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)
        time.sleep(2)
        start()


def time_converter():
    print("Input what you would like to convert from")
    print(colors.yellow, "Please stick to this format")
    print(colors.yellow, "XY XD XH XM XS (X is your number)\t ie: 10Y means 10 years.\n", colors.reset)

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

    convert_to = input("""(1) Years
(2) Days
(3) Minutes
(4) Seconds
What do you want to convert to: """)
    print()
    convert_to = int(convert_to)
    if convert_to == 1:
        print(colors.green, total_seconds / 31536000, "years\n", colors.reset)
        restart.restart()
    elif convert_to == 2:
        print(colors.green, total_seconds / 86400, "days\n", colors.reset)
        restart.restart()
    elif convert_to == 3:
        print(colors.green, total_seconds / 60, "minutes\n", colors.reset)
        restart.restart()
    elif convert_to == 4:
        print(colors.green, total_seconds, "seconds\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input...\n" + colors.reset)
        time.sleep(2)
        time_converter()


def bytes_converter():
    choice = float(input('How many Bytes: '))
    print()
    b_k = choice / 1000
    b_m = choice / 1e+6
    b_g = choice / 1e+9
    b_t = choice / 1e+12
    print(colors.green, choice, 'Bytes equals',
          b_k, 'in Kilobytes.')
    print(colors.green, choice, 'Bytes equals',
          b_m, 'in Megabytes.')
    print(colors.green, choice, 'Bytes equals',
          b_g, 'in Gigabytes.')
    print(colors.green, choice, 'Bytes equals',
          b_t, 'in Terabytes.\n', colors.reset)
    restart.restart()


def kilobytes_converter():
    choice = float(input('How many Kilobytes: '))
    print()
    k_b = choice * 1000
    k_m = choice / 1000
    k_g = choice / 1e+6
    k_t = choice / 1e+9
    print(colors.green, choice, 'Kilobytes equals',
          k_b, 'in Bytes.')
    print(colors.green, choice, 'Kilobytes equals',
          k_m, 'in Megabytes.')
    print(colors.green, choice, 'Kilobytes equals',
          k_g, 'in Gigabytes.')
    print(colors.green, choice, 'Kilobytes equals',
          k_t, 'in Terabytes.\n', colors.reset)
    restart.restart()


def megabytes_converter():
    choice = float(input('How many Megabytes: '))
    print()
    m_b = choice * 1e+6
    m_k = choice * 1000
    m_g = choice / 1000
    m_t = choice / 1e+6
    print(colors.green, choice, 'Megabytes equals',
          m_b, 'in Bytes.')
    print(colors.green, choice, 'Megabytes equals',
          m_k, 'in Kilobytes.')
    print(colors.green, choice, 'Megabytes equals',
          m_g, 'in Gigabytes.')
    print(colors.green, choice, 'Megabytes equals',
          m_t, 'in Terabytes.\n', colors.reset)
    restart.restart()


def gigabytes_converter():
    choice = float(input('How many Gigabytes: '))
    print()
    g_b = choice * 1e+9
    g_k = choice * 1e+6
    g_m = choice * 1000
    g_t = choice / 1000
    print(colors.green, choice, 'Gigabytes equals',
          g_b, 'in Bytes.')
    print(colors.green, choice, 'Gigabytes equals',
          g_k, 'in Kilobytes.')
    print(colors.green, choice, 'Gigabytes equals',
          g_m, 'in Megabytes.')
    print(colors.green, choice, 'Gigabytes equals',
          g_t, 'in Terabytes.\n', colors.reset)
    restart.restart()


def terabytes_converter():
    choice = float(input('How many Terabytes: '))
    print()
    t_b = choice * 1e+12
    t_k = choice * 1e+9
    t_m = choice * 1e+6
    t_g = choice * 1000
    print(colors.green, choice, 'Terabytes equals',
          t_b, 'in Bytes.')
    print(colors.green, choice, 'Terabytes equals',
          t_k, 'in Kilobytes.')
    print(colors.green, choice, 'Terabytes equals',
          t_m, 'in Megabytes.')
    print(colors.green, choice, 'Terabytes equals',
          t_g, 'in Gigabytes.\n', colors.reset)
    restart.restart()


def storage_converter():
    choice = int(input("""(1) Bytes to All
(2) Kilobytes to ALL
(3) Megabytes to ALL
(4) Gigabyte to ALL
(5) Terabyte to ALL
Which calculation would you like to perform: """))
    print()

    if choice == 1:
        bytes_converter()
    elif choice == 2:
        kilobytes_converter()
    elif choice == 3:
        megabytes_converter()
    elif choice == 4:
        gigabytes_converter()
    elif choice == 5:
        terabytes_converter()
    else:
        print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)
        time.sleep(2)
        storage_converter()


def pressure_converter():
    user_choice = int(input("""
        (1) Pascal [Pa] to All
        (2) Kilopascal [kPa] to ALL
        (3) bar to ALL
        (4) Standard atmosphere [atm] to ALL
        Which calculation would you like to perform: """))
    print()
    if user_choice == 1:
        pressure = float(input("Enter Pressure amount: "))
        print()
        pr_to_kpa = float(pressure / 1000)
        pr_to_bar = float(pressure / 100000)
        pr_to_atm = float(pressure / 101325)
        print(colors.green, pressure, "in pascal [Pa] equals",
              pr_to_kpa, "in kilopascal [kPa].")
        print(colors.green, pressure, "in pascal [Pa] equals",
              pr_to_bar, "in bar.")
        print(colors.green, pressure, "in pascal [Pa] equals",
              pr_to_atm, "in Standard atmosphere [atm].\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        pressure = float(input("Enter Pressure amount: "))
        print()
        kp_to_p = float(pressure * 1000)
        kp_to_bar = float(pressure / 100)
        kp_to_atm = float(pressure / 101)
        print(colors.green, pressure, "in kilopascal [kPa] equals",
              kp_to_p, "in pascal [Pa].")
        print(colors.green, pressure, "in kilopascal [kPa] equals",
              kp_to_bar, "in bar.")
        print(colors.green, pressure, "in kilopascal [kPa] equals",
              kp_to_atm, "in Standard atmosphere [atm].\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        pressure = float(input("Enter Pressure amount: "))
        print()
        bar_to_p = float(pressure * 100000)
        bar_to_kpa = float(pressure * 100)
        bar_to_atm = float(pressure / 1013)
        print(colors.green, pressure, "in bar equals",
              bar_to_p, "in pascal [Pa].")
        print(colors.green, pressure, "in bar equals",
              bar_to_kpa, "in kilopascal [kPa].")
        print(colors.green, pressure, "in bar equals",
              bar_to_atm, "in Standard atmosphere [atm].\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        pressure = float(input("Enter Pressure amount: "))
        print()
        atm_to_p = float(pressure * 101325)
        atm_to_kpa = float(pressure * 101)
        atm_to_bar = float(pressure * 1013)
        print(colors.green, pressure, "in Standard atmosphere [atm] equals",
              atm_to_p, "in pascal [Pa].")
        print(colors.green, pressure, "in Standard atmosphere [atm] equals",
              atm_to_kpa, "in kilopascal [kPa].")
        print(colors.green, pressure, "in Standard atmosphere [atm] equals",
              atm_to_bar, "in bar.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        pressure_converter()


def angle_converter():
    user_choice = int(input("""
            (1) Degree [°] to All
            (2) Radian [rad] to ALL
            (3) grad [^g] to ALL
            (4) Minute ['] to ALL
            Which calculation would you like to perform: """))
    print()
    if user_choice == 1:
        angle = float(input("Enter the angle: "))
        print()
        ang_to_rad = float(angle * (3.14 / 180))
        ang_to_grad = float(angle * (200 / 180))
        ang_to_min = float(angle * 60)
        print(colors.green, angle, "in Degree [°] equals",
              ang_to_rad, "in Radian [rad].")
        print(colors.green, angle, "in Degree [°] equals",
              ang_to_grad, "in grad [^g].")
        print(colors.green, angle, "in Degree [°] equals",
              ang_to_min, "in Minute ['].\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        angle = float(input("Enter the angle: "))
        print()
        ang_to_deg = float(angle * (180 / 3.14))
        ang_to_grad = float(angle * (200 / 3.14))
        ang_to_min = float(angle * 3437.75)
        print(colors.green, angle, "in Radian [rad] equals",
              ang_to_deg, "in Degree [°].")
        print(colors.green, angle, "in Radian [rad] equals",
              ang_to_grad, "in grad [^g].")
        print(colors.green, angle, "in Radian [rad] equals",
              ang_to_min, "in Minute ['].\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        angle = float(input("Enter the angle: "))
        print()
        ang_to_deg = float(angle * 0.9)
        ang_to_rad = float(angle * 0.015708)
        ang_to_min = float(angle * 54)
        print(colors.green, angle, "in grad [^g] equals",
              ang_to_deg, "in Degree [°].")
        print(colors.green, angle, "in grad [^g] equals",
              ang_to_rad, "in Radian [rad].")
        print(colors.green, angle, "in grad [^g] equals",
              ang_to_min, "in Minute ['].\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        angle = float(input("Enter the angle: "))
        print()
        ang_to_deg = float(angle * 0.0166667)
        ang_to_rad = float(angle * 0.0002908882)
        ang_to_grad = float(angle * 0.0185185185)
        print(colors.green, angle, "in Minute ['] equals",
              ang_to_deg, "in Degree [°].")
        print(colors.green, angle, "in Minute ['] equals",
              ang_to_rad, "in Radian [rad].")
        print(colors.green, angle, "in Minute ['] equals",
              ang_to_grad, "in grad [^g].\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        angle_converter()


def energy_converter():
    choice = int(input('''(1) Joule to ALL
(2) KiloJoule to ALL
(3) Watt Hour to ALL
(4) Kilowatt Hour to ALL
Which energy conversion would you like to pick: '''))
    print()
    if choice == 1:
        j = float(input("Joules: "))
        print()
        j_to_kj = float(j / 1000)
        j_to_w = float(j / 3600)
        j_to_kw = float(j / 3.6e+6)
        print(colors.green, j, "in Joules equals",
              j_to_kj, "in Kilojoules.")
        print(colors.green, j, "in Joules equals",
              j_to_w, "in Watts.")
        print(colors.green, j, "in Joules equals",
              j_to_kw, "in Kilowatts.\n", colors.reset)
        restart.restart()
    elif choice == 2:
        kj = float(input("Kilojoules: "))
        print()
        kj_to_j = float(kj * 1000)
        kj_to_w = float(kj / 3.6)
        kj_to_kw = float(kj / 3600)
        print(colors.green, kj, "in Kilojoules equals",
              kj_to_j, "in Kilojoules.")
        print(colors.green, kj, "in Kilojoules equals",
              kj_to_w, "in Watts.")
        print(colors.green, kj, "in Kilojoules equals",
              kj_to_kw, "in Kilowatts.\n", colors.reset)
        restart.restart()
    elif choice == 3:
        w = float(input("Watts: "))
        print()
        w_to_j = float(w * 3600)
        w_to_kj = float(w * 3.6)
        w_to_kw = float(w / 1000)
        print(colors.green, w, "in Watts equals",
              w_to_j, "in Joules.")
        print(colors.green, w, "in Watts equals",
              w_to_kj, "in Kilojoules.")
        print(colors.green, w, "in Watts equals",
              w_to_kw, "in Kilowatts.\n", colors.reset)
        restart.restart()
    elif choice == 4:
        kw = float(input("Kilowatts: "))
        print()
        kw_to_j = float(kw * 3.6e+6)
        kw_to_kj = float(kw * 3600)
        kw_to_w = float(kw * 1000)
        print(colors.green, kw, "in Kilowatts equals",
              kw_to_j, "in Joules.")
        print(colors.green, kw, "in Kilowatts equals",
              kw_to_kj, "in Kilojoules.")
        print(colors.green, kw, "in Kilowatts equals",
              kw_to_w, "in Watts.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        energy_converter()


def fuel_converter():
    choice = int(input('''(1) Miles Per Gallon to ALL
(2) Miles Per Gallon (Imperial) to ALL
(3) Kilometers Per Liter to ALL
Which Fuel Economy convertion would you like to pick: '''))
    print()
    if choice == 1:
        mpg = float(input("Miles Per Gallon: "))
        print()
        mpg_to_mpgi = float(mpg * 1.201)
        mpg_to_kpl = float(mpg / 2.352)
        print(colors.green, mpg, "in Miles Per Gallon equals",
              mpg_to_mpgi, "in Miles Per Gallon (Imperial).")
        print(colors.green, mpg, "in Miles Per Gallon equals",
              mpg_to_kpl, "in Kilometers Per Liter.\n", colors.reset)
        restart.restart()
    elif choice == 2:
        mpgi = float(input("Miles Per Gallon (Imperial): "))
        print()
        mpgi_to_mpg = float(mpgi / 1.201)
        mpgi_to_kpl = float(mpgi / 2.825)
        print(colors.green, mpgi, "in Miles Per Gallon (Imperial) equals",
              mpgi_to_mpg, "in Miles Per Gallon.")
        print(colors.green, mpgi, "in Miles Per Gallon (Imperial) equals",
              mpgi_to_kpl, "in Kilometers Per Liter.\n", colors.reset)
        restart.restart()
    elif choice == 3:
        kpl = float(input("Kilometers Per Liter: "))
        print()
        mpgi_to_mpg = float(kpl * 2.352)
        mpgi_to_mpgi = float(kpl * 2.825)
        print(colors.green, kpl, "in Kilometers Per Liter equals",
              mpgi_to_mpg, "in Miles Per Gallon.")
        print(colors.green, kpl, "in Kilometers Per Liter equals",
              mpgi_to_mpgi, "in Miles Per Gallon (Imperial).\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        fuel_converter()


def frequency_converter():
    choice = int(input('''(1) Hertz to ALL
(2) Kilohertz to ALL
(3) Megahertz to ALL
(4) Gigahertz to ALL
Which Sound Frequency convertion would you like to pick: '''))
    print()
    if choice == 1:
        h = float(input("Hertz: "))
        print()
        h_to_kh = float(h / 1000)
        h_to_mh = float(h / 1e+6)
        h_to_gh = float(h / 1e+9)
        print(colors.green, h, "in Hertz equals",
              h_to_kh, "in Kilohertz.")
        print(colors.green, h, "in Hertz equals",
              h_to_mh, "in Megahertz.")
        print(colors.green, h, "in Hertz equals",
              h_to_gh, "in Gigahertz.\n", colors.reset)
        restart.restart()
    elif choice == 2:
        kh = float(input("Kilohertz: "))
        print()
        kh_to_h = float(kh * 1000)
        kh_to_mh = float(kh / 1000)
        kh_to_gh = float(kh / 1e+6)
        print(colors.green, kh, "in Kilohertz equals",
              kh_to_h, "in Hertz.")
        print(colors.green, kh, "in Kilohertz equals",
              kh_to_mh, "in Megahertz.")
        print(colors.green, kh, "in Kilohertz equals",
              kh_to_gh, "in Gigahertz.\n", colors.reset)
        restart.restart()
    elif choice == 3:
        mh = float(input("Megahertz: "))
        print()
        mh_to_h = float(mh * 1e+6)
        mh_to_kh = float(mh * 1000)
        mh_to_gh = float(mh / 1000)
        print(colors.green, mh, "in Megahertz equals",
              mh_to_h, "in Hertz.")
        print(colors.green, mh, "in Megahertz equals",
              mh_to_kh, "in Kilohertz.")
        print(colors.green, mh, "in Megahertz equals",
              mh_to_gh, "in Gigahertz.\n", colors.reset)
        restart.restart()
    elif choice == 4:
        gh = float(input("Gigahertz: "))
        print()
        gh_to_h = float(gh * 1e+9)
        gh_to_kh = float(gh * 1e+6)
        gh_to_mh = float(gh * 1000)
        print(colors.green, gh, "in Gigahertz equals",
              gh_to_h, "in Hertz.")
        print(colors.green, gh, "in Gigahertz equals",
              gh_to_kh, "in Kilohertz.")
        print(colors.green, gh, "in Gigahertz equals",
              gh_to_mh, "in Megahertz.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        frequency_converter()


def start():
    choice = int(input('''
(1) Temperature Converter
(2) Mass Converter
(3) Length Converter
(4) Volume Converter
(5) Currency Converter
(6) Crypto Converter
(7) Speed Converter
(8) Digital Storage Converter
(9) Time Converter
(10) Pressure Converter
(11) Angle Converter
(12) Energy Converter
(13) Fuel Economy Converter
(14) Sound Frequency Converter
(15) Restart
(16) Quit
What converter would you like to perform: '''))
    print()

    if choice == 1:
        temp_converter()
    elif choice == 2:
        mass_converter()
    elif choice == 3:
        length_converter()
    elif choice == 4:
        volume_converter()
    elif choice == 5:
        currency_converter()
    elif choice == 6:
        crypto_converter()
    elif choice == 7:
        speed_converter()
    elif choice == 8:
        storage_converter()
    elif choice == 9:
        time_converter()
    elif choice == 10:
        pressure_converter()
    elif choice == 11:
        angle_converter()
    elif choice == 12:
        energy_converter()
    elif choice == 13:
        fuel_converter()
    elif choice == 14:
        frequency_converter()
    elif choice == 15:
        restart.restart()
    elif choice == 16:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        time.sleep(2)
        start()


if __name__ == '__main__':
    length_converter()

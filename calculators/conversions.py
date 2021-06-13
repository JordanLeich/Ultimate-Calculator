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
        print(f"{user_celsius} Celsius is {kelvin} in Kelvin. {colors.reset}\n")
        restart.restart()
    elif user_choice == 2:
        user_fahrenheit = repeat_input("Fahrenheit: ", "Invalid Number...\n", "float")
        print()

        celsius, kelvin = fahrenheit_to_all(user_fahrenheit)
        print(f"{colors.green}{user_fahrenheit} Fahrenheit is {celsius} in Celsius.")
        print(f"{user_fahrenheit} Fahrenheit is {kelvin} in Kelvin. {colors.reset}\n")
        restart.restart()
    elif user_choice == 3:
        user_kelvin = repeat_input("Kelvin: ", "Invalid Number...\n", "float")
        print()

        celsius, fahrenheit = kelvin_to_all(user_kelvin)
        print(f"{colors.green}{user_kelvin} Kelvin is {celsius} in Celsius.")
        print(f"{user_kelvin} Kelvin is {fahrenheit} in Fahrenheit. {colors.reset}\n")
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
        print(f'{feet} in Feet equals {yard} in Yards.')
        print(f'{feet} in Feet equals {mile} in Miles.{colors.reset}\n')
        restart.restart()

    elif user_choice == 2:
        inch = repeat_input("Inches: ", "Invalid Number...\n", "float")
        print()

        feet, yard, mile = inches_to_all(inch)
        print(f'{colors.green}{inch} in Inches equals {feet} in Feet.')
        print(f'{inch} in Inches equals {yard} in Yards.')
        print(f'{inch} in Inches equals {mile} in Miles.{colors.reset}\n')
        restart.restart()

    elif user_choice == 3:
        yard = repeat_input("Yards: ", "Invalid Number...\n", "float")
        print()

        feet, inch, mile = yards_to_all(yard)
        print(f'{colors.green}{yard} in Yards equals {feet} in Feet.')
        print(f'{yard} in Yards equals {inch} in Inches.')
        print(f'{yard} in Yards equals {mile} in Miles.{colors.reset}\n')
        restart.restart()

    elif user_choice == 4:
        mile = float(input("Miles: "))
        print()

        feet, inch, yard = miles_to_all(mile)
        print(f'{colors.green}{mile} in Miles equals {feet} in Feet.')
        print(f'{mile} in Miles equals {inch} in Inches.')
        print(f'{mile} in Miles equals {yard} in Yards.{colors.reset}\n')
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
        print(f'{gallon} in Gallons equals {pint} in Pints.')
        print(f'{gallon} in Gallons equals {ounce} in Ounces. {colors.reset}\n')
        restart.restart()

    elif user_choice == 4:
        quart = repeat_input("Quarts: ", "Invalid Number...\n", "float")
        print()

        gallon, pint, ounce = quarts_to_all(quart)
        print(f'{colors.green}{quart} in Quarts equals {gallon} in Gallons.')
        print(f'{quart} in Quarts equals {pint} in Pints.')
        print(f'{quart} in Quarts equals {ounce} in Ounces. {colors.reset}\n')
        restart.restart()

    elif user_choice == 5:
        pint = repeat_input("Pints: ", "Invalid Number...\n", "float")
        print()

        gallon, quart, ounce = pints_to_all(pint)
        print(f'{colors.green}{pint} in Pints equals {gallon} in Gallons.')
        print(f'{pint} in Pints equals {quart} in Quarts.')
        print(f'{pint} in Pints equals {ounce} in Ounces. {colors.reset}\n')
        restart.restart()

    elif user_choice == 6:
        ounce = repeat_input("Ounces: ", "Invalid Number...\n", "float")
        print()

        gallon, quart, pint = ounces_to_all2(ounce)
        print(f'{colors.green}{ounce} in Ounces equals {gallon} in Gallons.')
        print(f'{ounce} in Ounces equals {quart} in Quarts.')
        print(f'{ounce} in Ounces equals {pint} in Pints. {colors.reset}\n')
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        volume_converter()


# Crypto
def bitcoin_to_all(data):
    data = float(data)

    ethereum = data * 13.72
    dogecoin = data * 95317.32
    shiba_inu = data * 4.03

    return ethereum, dogecoin, shiba_inu


def ethereum_to_all(data):
    data = float(data)

    bitcoin = data * 0.072
    dogecoin = data * 6686.2
    shiba_inu = data * 292.12

    return bitcoin, dogecoin, shiba_inu


def dogecoin_to_all(data):
    data = float(data)

    bitcoin = data * 0.00001089
    ethereum = data * 0.000150
    shiba_inu = data * 43745

    return bitcoin, ethereum, shiba_inu


def shiba_inu_to_all(data):
    data = float(data)

    bitcoin = data * 0.00000001
    ethereum = data * 0.0000000012
    dogecoin = data * 0.000023

    return bitcoin, ethereum, dogecoin


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
        bitcoin = repeat_input("Bitcoin Amount: ", "Invalid Number...\n", "float")
        print()

        ethereum, dogecoin, shiba_inu = bitcoin_to_all(bitcoin)
        print(f'{colors.green}{bitcoin} in Bitcoin equals {ethereum} in Ethereum.')
        print(f'{bitcoin} in Bitcoin equals {dogecoin} in DogeCoin.')
        print(f'{bitcoin} in Bitcoin equals {shiba_inu} in SHIBA INU. {colors.reset}\n')
        restart.restart()

    elif user_choice == 2:
        ethereum = repeat_input("Ethereum Amount: ", "Invalid Number...\n", "float")
        print()

        bitcoin, dogecoin, shiba_inu = ethereum_to_all(ethereum)
        print(f'{colors.green}{ethereum} in Ethereum equals {bitcoin} in Bitcoin.')
        print(f'{ethereum} in Ethereum equals {dogecoin} in DogeCoin.')
        print(f'{ethereum} in Ethereum equals {shiba_inu} in SHIBA INU. {colors.reset}\n')
        restart.restart()

    elif user_choice == 3:
        dogecoin = repeat_input("DogeCoin Amount: ", "Invalid Number...\n", "float")
        print()

        bitcoin, ethereum, shiba_inu = bitcoin_to_all(dogecoin)
        print(f'{colors.green}{dogecoin} in DogeCoin equals {bitcoin} in Bitcoin.')
        print(f'{dogecoin} in DogeCoin equals {ethereum} in Ethereum.')
        print(f'{dogecoin} in DogeCoin equals {shiba_inu} in SHIBA INU. {colors.reset}\n')
        restart.restart()

    elif user_choice == 4:
        shiba_inu = float(input("SHIBA INU Amount: "))
        print()

        bitcoin, ethereum, dogecoin = shiba_inu_to_all(shiba_inu)
        print(f'{colors.green}{shiba_inu} in DogeCoin equals {bitcoin} in Bitcoin.')
        print(f'{shiba_inu} in DogeCoin equals {ethereum} in Ethereum.')
        print(f'{shiba_inu} in DogeCoin equals {dogecoin} in DogeCoin. {colors.reset}\n')
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        crypto_converter()


# Speed
def mph_to_all(data):
    data = float(data)

    fps = data * 1.467
    mps = data / 2.237
    kph = data * 1.609
    knot = data / 1.151

    return fps, mps, kph, knot


def fps_to_all(data):
    data = float(data)

    mph = data / 1.467
    mps = data / 3.281
    kph = data * 1.097
    knot = data / 1.688

    return mph, mps, kph, knot


def mps_to_all(data):
    data = float(data)

    mph = data * 2.237
    fps = data * 3.281
    kph = data * 3.6
    knot = data * 1.944

    return mph, fps, kph, knot


def kph_to_all(data):
    data = float(data)

    mph = data / 1.609
    fps = data / 1.097
    mps = data / 3.6
    knot = data / 1.852

    return mph, fps, mps, knot


def knot_to_all(data):
    data = float(data)

    mph = data * 1.151
    fps = data * 1.688
    mps = data / 1.944
    kph = data * 1.852

    return mph, fps, mps, kph


def speed_converter():
    """
    Handles all speed conversion
    """
    choice = int(input("""(1) Miles Per Hour to All
(2) Foot Per Second to ALL
(3) Meter Per Second to ALL
(4) Kilometer Per Hour to ALL
(5) Knot to ALL
Which calculation would you like to perform: """))
    print()

    if choice == 1:
        mph = repeat_input('How many Miles Per Hour: ', "Invalid Number...\n", "float")
        print()

        fps, mps, kph, knot = mph_to_all(mph)
        print(f'{colors.green}{mph} Miles Per Hour equals {fps} in Foot Per Second.')
        print(f'{mph} Miles Per Hour equals {mps} in Meters Per Second.')
        print(f'{mph} Miles Per Hour equals {kph} in Kilometers Per Hour.')
        print(f'{mph} Miles Per Hour equals {knot} in Knot. {colors.reset}\n')
        restart.restart()

    elif choice == 2:
        fps = repeat_input('How many Foot Per Second: ', "Invalid Number...\n", "float")
        print()

        mph, mps, kph, knot = fps_to_all(fps)
        print(f'{colors.green}{fps} Foot Per Second equals {mph} in Miles Per Hour.')
        print(f'{fps} Foot Per Second equals {mps} in Meters Per Second.')
        print(f'{fps} Foot Per Second equals {kph} in Kilometers Per Hour.')
        print(f'{fps} Foot Per Seconds equals {knot} in Knot. {colors.reset}\n')
        restart.restart()

    elif choice == 3:
        mps = repeat_input('How many Meters Per Second: ', "Invalid Number...\n", "float")
        print()

        mph, fps, kph, knot = mps_to_all(mps)
        print(f'{colors.green}{mps} Meters Per Second equals {mph} in Miles Per Hour.')
        print(f'{mps} Meters Per Second equals {fps} in Foot Per Second.')
        print(f'{mps} Meters Per Second equals {kph} in Kilometers Per Hour.')
        print(f'{mps} Meters Per Second equals {knot} in Knot. {colors.reset}\n')
        restart.restart()

    elif choice == 4:
        kph = repeat_input('How many Kilometers Per Hour: ', "Invalid Number...\n", "float")
        print()

        mph, fps, mps, knot = kph_to_all(kph)
        print(f'{colors.green}{kph} Kilometers Per Hour equals {mph} in Miles Per Hour.')
        print(f'{kph} Kilometers Per Hour equals {fps} in Foot Per Second.')
        print(f'{kph} Kilometers Per Hour equals {mps} in Meters Per Second.')
        print(f'{kph} Kilometers Per Hour equals {knot} in Knot. {colors.reset}\n')
        restart.restart()

    elif choice == 5:
        knot = repeat_input('How many Knots: ', "Invalid Number...\n", "float")
        print()

        mph, fps, mps, kph = knot_to_all(knot)
        print(f'{colors.green}{knot} Meters Per Second equals {mph} in Miles Per Hour.')
        print(f'{knot} Knots equals {fps} in Foot Per Second.')
        print(f'{knot} Knots equals {mps} in Meters Per Second.')
        print(f'{knot} Knots {kph} in Kilometers Per Hour. {colors.reset}\n')
        restart.restart()

    else:
        print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)
        time.sleep(2)
        start()


# Time
def time_converter():
    print("Input what you would like to convert from")
    print(f'{colors.yellow}Please stick to this format')
    print(f'XY XD XH XM XS (X is your number)\t ie: 10Y means 10 years. {colors.reset}\n')

    response = input('Time: ').replace(" ", '')
    time_format = response[-1].lower()
    total_seconds = int(response[:-1])

    if time_format.endswith('m'):
        total_seconds *= 60
    elif time_format.endswith('h'):
        total_seconds *= 3600
    elif time_format.endswith('d'):
        total_seconds *= 86400
    elif time_format.endswith('y'):
        total_seconds *= 31536000

    convert_to = input("""(1) Years
(2) Days
(3) Minutes
(4) Seconds
What do you want to convert to: """)

    if convert_to == '1':
        print(colors.green, total_seconds / 31536000, "years\n", colors.reset)
        restart.restart()

    elif convert_to == '2':
        print(colors.green, total_seconds / 86400, "days\n", colors.reset)
        restart.restart()

    elif convert_to == "3":
        print(colors.green, total_seconds / 60, "minutes\n", colors.reset)
        restart.restart()

    elif convert_to == "4":
        print(colors.green, total_seconds, "seconds\n", colors.reset)
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input...\n" + colors.reset)
        time.sleep(2)
        time_converter()


# Storage
def bytes_converter(data):
    data = float(data)

    kilobyte = data / 1000
    megabyte = data / 1e+6
    gigabyte = data / 1e+9
    terabyte = data / 1e+12

    return kilobyte, megabyte, gigabyte, terabyte


def kilobytes_converter(data):
    data = float(data)

    byte = data * 1000
    megabyte = data / 1000
    gigabyte = data / 1e+6
    terabyte = data / 1e+9

    return byte, megabyte, gigabyte, terabyte


def megabytes_converter(data):
    data = float(data)

    byte = data * 1e+6
    kilobyte = data * 1000
    gigabyte = data / 1000
    terabyte = data / 1e+6

    return byte, kilobyte, gigabyte, terabyte


def gigabytes_converter(data):
    data = float(data)

    byte = data * 1e+9
    kilobyte = data * 1e+6
    megabyte = data * 1000
    terabyte = data / 1000

    return byte, kilobyte, megabyte, terabyte


def terabytes_converter(data):
    data = float(data)

    byte = data * 1e+12
    kilobyte = data * 1e+9
    megabyte = data * 1e+6
    gigabyte = data * 1000

    return byte, kilobyte, megabyte, gigabyte


def storage_converter():
    choice = int(input("""(1) Bytes to All
(2) Kilobytes to ALL
(3) Megabytes to ALL
(4) Gigabyte to ALL
(5) Terabyte to ALL
Which calculation would you like to perform: """))
    print()

    if choice == 1:
        byte = repeat_input("Bytes: ", "Invalid Number...\n", "float")
        print()

        kilobyte, megabyte, gigabyte, terabyte = bytes_converter(byte)
        print(f'{colors.green}{byte} Bytes equals {kilobyte} in Kilobytes.')
        print(f'{colors.green}{byte} Bytes equals {megabyte} in Megabytes.')
        print(f'{colors.green}{byte} Bytes equals {gigabyte} in Gigabytes.')
        print(f'{colors.green}{byte} Bytes equals {terabyte} in Terabytes. {colors.reset}\n')
        restart.restart()

    elif choice == 2:
        kilobyte = repeat_input("Kilobytes: ", "Invalid Number...\n", "float")
        print()

        byte, megabyte, gigabyte, terabyte = kilobytes_converter(kilobyte)
        print(f'{colors.green}{kilobyte} Kilobytes equals {byte} in Bytes.')
        print(f'{colors.green}{kilobyte} Kilobytes equals {megabyte} in Megabytes.')
        print(f'{colors.green}{kilobyte} Kilobytes equals {gigabyte} in Gigabytes.')
        print(f'{colors.green}{kilobyte} Kilobytes equals {terabyte} in Terabytes. {colors.reset}\n')
        restart.restart()

    elif choice == 3:
        megabyte = repeat_input("Megabytes: ", "Invalid Number...\n", "float")
        print()

        byte, kilobyte, gigabyte, terabyte = megabytes_converter(megabyte)
        print(f'{colors.green}{megabyte} Megabytes equals {byte} in Bytes.')
        print(f'{colors.green}{megabyte} Megabytes equals {kilobyte} in Kilobytes.')
        print(f'{colors.green}{megabyte} Megabytes equals {gigabyte} in Gigabytes.')
        print(f'{colors.green}{megabyte} Megabytes equals {terabyte} in Terabytes. {colors.reset}\n')
        restart.restart()

    elif choice == 4:
        gigabyte = repeat_input("Gigabytes: ", "Invalid Number...\n", "float")
        print()

        byte, kilobyte, megabyte, terabyte = gigabytes_converter(gigabyte)
        print(f'{colors.green}{gigabyte} Gigabytes equals {byte} in Bytes.')
        print(f'{colors.green}{gigabyte} Gigabytes equals {kilobyte} in Kilobytes.')
        print(f'{colors.green}{gigabyte} Gigabytes equals {megabyte} in Megabytes.')
        print(f'{colors.green}{gigabyte} Gigabytes equals {terabyte} in Terabytes. {colors.reset}\n')
        restart.restart()

    elif choice == 5:
        terabyte = repeat_input("Terabytes: ", "Invalid Number...\n", "float")
        print()

        byte, kilobyte, megabyte, gigabyte = terabytes_converter(terabyte)
        print(f'{colors.green}{terabyte} Terabytes equals {byte} in Bytes.')
        print(f'{colors.green}{terabyte} Terabytes equals {kilobyte} in Kilobytes.')
        print(f'{colors.green}{terabyte} Terabytes equals {megabyte} in Megabytes.')
        print(f'{colors.green}{terabyte} Terabytes equals {gigabyte} in Gigabytes. {colors.reset}\n')
        restart.restart()

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
    time_converter()

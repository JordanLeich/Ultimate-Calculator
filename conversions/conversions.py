import time
try:
    import winsound
    windows = True
except:
    linux = True

from docx2pdf import convert
from moviepy.editor import *
from modules import restart, end, colors
from modules.currency_api import get_currency, validate_key
from modules.tools import repeat_input
import json


def currency_converter():
    with open("../key.json", 'r') as json_file:
        data = json.load(json_file)
        api_key = data["key"]
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
        print()
        d_to_e = float(user_dollar * get_currency("USD_EUR", api_key))
        d_to_j = float(user_dollar * get_currency("USD_JPY", api_key))
        d_to_c = float(user_dollar * get_currency("USD_CAD", api_key))
        d_to_mad = float(user_dollar * get_currency("USD_MAD", api_key))
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
        e_to_d = float(user_euro * get_currency("EUR_USD", api_key))
        e_to_j = float(user_euro * get_currency("EUR_JPY", api_key))
        e_to_c = float(user_euro * get_currency("EUR_CAD", api_key))
        e_to_mad = float(user_euro * get_currency("EUR_MAD", api_key))
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
        c_to_d = float(user_canadian * get_currency("CAD_USD", api_key))
        c_to_j = float(user_canadian * get_currency("CAD_JPY", api_key))
        c_to_e = float(user_canadian * get_currency("CAD_EUR", api_key))
        c_to_mad = float(user_canadian * get_currency("CAD_MAD", api_key))
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
        y_to_d = float(user_yen * get_currency("JPY_USD", api_key))
        y_to_e = float(user_yen * get_currency("JPY_EUR", api_key))
        y_to_c = float(user_yen * get_currency("JPY_CAD", api_key))
        y_to_mad = float(user_yen * get_currency("JPY_MAD", api_key))
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
        mad_to_d = float(user_mad * get_currency("MAD_USD", api_key))
        mad_to_e = float(user_mad * get_currency("MAD_EUR", api_key))
        mad_to_c = float(user_mad * get_currency("MAD_CAD", api_key))
        mad_to_yen = float(user_mad * get_currency("MAD_JPY", api_key))
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
        input("""(1) Celsius to ALL
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
    """
    Handles all time conversion
    """
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
    """
    Handles all speed conversion
    """
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


# Pressure
def pascal_to_all(data):
    data = float(data)

    kpa = data / 1000
    bar = data / 100000
    atm = data / 101325

    return kpa, bar, atm


def kilopascal_to_all(data):
    data = float(data)

    pa = data * 1000
    bar = data / 100
    atm = data / 101

    return pa, bar, atm


def bar_to_all(data):
    data = float(data)

    pa = data * 100000
    kpa = data * 100
    atm = data / 1013

    return pa, kpa, atm


def atm_to_all(data):
    data = float(data)

    pa = data * 101325
    kpa = data * 101
    bar = data * 1013

    return pa, kpa, bar


def pressure_converter():
    """
    Handles all pressure conversion
    """
    user_choice = int(input("""
(1) Pascal [Pa] to All
(2) Kilopascal [kPa] to ALL
(3) bar to ALL
(4) Standard atmosphere [atm] to ALL

Which calculation would you like to perform: """))
    print()

    if user_choice == 1:
        pa = repeat_input("Enter Pressure amount: ", "Invalid Number...\n", "float")
        print()

        kpa, bar, atm = pascal_to_all(pa)
        print(f'{colors.green}{pa} in pascal [Pa] equals {kpa} in kilopascal [kPa].')
        print(f'{pa} in pascal [Pa] equals {bar} in bar.')
        print(f'{pa} in pascal [Pa] equals {atm} in Standard atmosphere [atm]. {colors.reset}\n')
        restart.restart()

    elif user_choice == 2:
        kilopascal = repeat_input("Enter Pressure amount: ", "Invalid Number...\n", "float")
        print()

        pa, bar, atm = kilopascal_to_all(kilopascal)
        print(f'{colors.green}{kilopascal} in pascal [Pa] equals {pa} in pascal [Pa].')
        print(f'{kilopascal} in pascal [Pa] equals {bar} in bar.')
        print(f'{kilopascal} in pascal [Pa] equals {atm} in Standard atmosphere [atm]. {colors.reset}\n')
        restart.restart()

    elif user_choice == 3:
        bar = repeat_input("Enter Pressure amount: ", "Invalid Number...\n", "float")
        print()

        pa, kpa, atm = kilopascal_to_all(bar)
        print(f'{colors.green}{bar} in pascal [Pa] equals {pa} in pascal [Pa].')
        print(f'{bar} in pascal [Pa] equals {kpa} kilopascal [kPa].')
        print(f'{bar} in pascal [Pa] equals {atm} in Standard atmosphere [atm]. {colors.reset}\n')
        restart.restart()

    elif user_choice == 4:
        atm = repeat_input("Enter Pressure amount: ", "Invalid Number...\n", "float")
        print()

        pa, kpa, bar = atm_to_all(atm)
        print(f'{colors.green}{bar} in pascal [Pa] equals {pa} in pascal [Pa].')
        print(f'{bar} in pascal [Pa] equals {kpa} kilopascal [kPa].')
        print(f'{bar} in pascal [Pa] equals {bar} in in bar. {colors.reset}\n')
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        pressure_converter()


# Angle
def degree_to_all(data):
    data = float(data)

    rad = data * (3.14 / 180)
    grad = data * (200 / 180)
    minute = data * 60

    return rad, grad, minute


def radian_to_all(data):
    data = float(data)

    deg = data * (180 / 3.14)
    grad = data * (200 / 3.14)
    minute = data * 3437.75

    return deg, grad, minute


def grad_to_all(data):
    data = float(data)

    deg = data * 0.9
    rad = data * 0.015708
    minute = data * 54

    return deg, rad, minute


def minute_to_all(data):
    data = float(data)

    deg = data * 0.0166667
    rad = data * 0.0002908882
    grad = data * 0.0185185185

    return deg, rad, grad


def angle_converter():
    """
    Handles all angle conversion
    """
    user_choice = int(input("""
(1) Degree [°] to All
(2) Radian [rad] to ALL
(3) grad [^g] to ALL
(4) Minute ['] to ALL

Which calculation would you like to perform: """))
    print()
    if user_choice == 1:
        deg = repeat_input("Enter the angle: ", "Invalid Number...\n", "float")
        print()

        rad, grad, minute = degree_to_all(deg)
        print(f'{colors.green}{deg} in Degree [°] equals {rad} in Radian [rad].')
        print(f'{deg} in Degree [°] equals {grad} in grad [^g].')
        print(f"{deg} in Degree [°] equals {minute} in Minute [']. {colors.reset}\n ")
        restart.restart()

    elif user_choice == 2:
        rad = repeat_input("Enter the angle: ", "Invalid Number...\n", "float")
        print()

        deg, grad, minute = radian_to_all(rad)
        print(f'{colors.green}{rad} in Radian [rad] equals {deg} in Degree [°].')
        print(f'{rad} in Radian [rad] equals {grad} in grad [^g].')
        print(f"{rad} in Radian [rad] equals {minute} in Minute [']. {colors.reset}\n ")
        restart.restart()

    elif user_choice == 3:
        grad = float(input("Enter the angle: "))
        print()

        deg, rad, minute = grad_to_all(grad)
        print(f'{colors.green}{grad} in grad [^g] equals {deg} in Degree [°].')
        print(f'{grad} in grad [^g] equals {rad} in Radian [rad].')
        print(f"{grad} in grad [^g] equals {minute} in Minute [']. {colors.reset}\n ")
        restart.restart()

    elif user_choice == 4:
        minute = float(input("Enter the angle: "))
        print()

        deg, rad, grad = minute_to_all(minute)
        print(f"{colors.green}{minute} in Minute ['] equals {deg} in Degree [°].")
        print(f"{minute} in Minute ['] equals {rad} in Radian [rad].")
        print(f"{minute} in Minute ['] equals {grad} in grad [^g]. {colors.reset}\n ")
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        angle_converter()


# Energy
def joule_to_all(data):
    data = float(data)

    kj = data / 1000
    w = data / 3600
    kw = data / 3.6e+6

    return kj, w, kw


def kj_to_all(data):
    data = float(data)

    j = data * 1000
    w = data / 3.6
    kw = data / 3600

    return j, w, kw


def w_to_all(data):
    data = float(data)

    j = data * 3600
    kj = data * 3.6
    kw = data / 1000

    return j, kj, kw


def kw_to_all(data):
    data = float(data)

    j = data * 3.6e+6
    kj = data * 3600
    w = data * 1000

    return j, kj, w


def energy_converter():
    """
    Handles all energy conversion
    """
    choice = int(input('''(1) Joule to ALL
(2) KiloJoule to ALL
(3) Watt Hour to ALL
(4) Kilowatt Hour to ALL

Which energy conversion would you like to pick: '''))
    print()
    if choice == 1:
        j = repeat_input("Joules: ", "Invalid Number...\n", "float")
        print()

        kj, w, kw = joule_to_all(j)
        print(f'{colors.green}{j} in Joules equals {kj} in Kilojoules.')
        print(f'{j} in Joules equals {w} in in Watts.')
        print(f'{j} in Joules equals {kw} in Kilowatts. {colors.reset}\n')
        restart.restart()

    elif choice == 2:
        kj = repeat_input("Kilojoules: ", "Invalid Number...\n", "float")
        print()

        j, w, kw = kj_to_all(kj)
        print(f'{colors.green}{kj} in Kilojoules equals {j} in Joules.')
        print(f'{kj} in Kilojoules equals {w} in in Watts.')
        print(f'{kj} in Kilojoules equals {kw} in Kilowatts. {colors.reset}\n')
        restart.restart()

    elif choice == 3:
        w = float(input("Watts: "))
        print()

        j, kj, kw = w_to_all(w)
        print(f'{colors.green}{w} in Watts equals {j} in Joules.')
        print(f'{w} in Watts equals {kj} in in Joules.')
        print(f'{w} in Watts equals {kw} in Kilowatts. {colors.reset}\n')
        restart.restart()

    elif choice == 4:
        kw = float(input("Kilowatts: "))
        print()

        j, kj, w = kw_to_all(kw)
        print(f'{colors.green}{kw} in Kilowatts equals {j} in Joules.')
        print(f'{kw} in Kilowatts equals {kj} in in Joules.')
        print(f'{kw} in Kilowatts equals {w} in Watts. {colors.reset}\n')
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        energy_converter()


#  Fuel
def mpg_to_all(data):
    data = float(data)

    mpgi = data * 1.201
    kpl = data / 2.352

    return mpgi, kpl


def mpgi_to_all(data):
    data = float(data)

    mpg = data / 1.201
    kpl = data / 2.825

    return mpg, kpl


def kpl_to_all(data):
    data = float(data)

    mpg = data * 2.352
    mpgi = data * 2.825

    return mpg, mpgi


def fuel_converter():
    """
    Handles all fuel conversion
    """
    choice = int(input('''(1) Miles Per Gallon to ALL
(2) Miles Per Gallon (Imperial) to ALL
(3) Kilometers Per Liter to ALL

Which Fuel Economy conversion would you like to pick: '''))
    print()
    if choice == 1:
        mpg = repeat_input("Miles Per Gallon: ", "Invalid Number...\n", "float")
        print()

        mpgi, kpl = mpg_to_all(mpg)
        print(f'{colors.green}{mpg} in Miles Per Gallon equals {mpgi} in Miles Per Gallon (Imperial).')
        print(f'{mpg} in Miles Per Gallon equals {kpl} in Kilometers Per Liter. {colors.reset}\n')
        restart.restart()

    elif choice == 2:
        mpgi = repeat_input("Miles Per Gallon (Imperial): ", "Invalid Number...\n", "float")
        print()

        mpg, kpl = mpgi_to_all(mpgi)
        print(f'{colors.green}{mpgi} in Miles Per Gallon (Imperial) equals {mpg} in Miles Per Gallon.')
        print(f'{mpgi} in Miles Per Gallon (Imperial) equals {kpl} in Kilometers Per Liter. {colors.reset}\n')
        restart.restart()

    elif choice == 3:
        kpl = repeat_input("Kilometers Per Liter: ", "Invalid Number...\n", "float")
        print()

        mpg, mpgi = kpl_to_all(kpl)
        print(f'{colors.green}{kpl} in Kilometers Per Liter equals {mpg} in Miles Per Gallon.')
        print(f'{kpl} inKilometers Per Liter equals {kpl} in Miles Per Gallon (Imperial). {colors.reset}\n')
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        fuel_converter()


# Frequency
def hertz_to_all(data):
    data = float(data)

    kilohertz = data / 1000
    megahertz = data / 1e+6
    gigahertz = data / 1e+9

    return kilohertz, megahertz, gigahertz


def kilohertz_to_all(data):
    data = float(data)

    hertz = data * 1000
    megahertz = data / 1000
    gigahertz = data / 1e+6

    return hertz, megahertz, gigahertz


def megahertz_to_all(data):
    data = float(data)

    hertz = data * 1e+6
    kilohertz = data * 1000
    gigahertz = data / 1000

    return hertz, kilohertz, gigahertz


def gigahertz_to_all(data):
    data = float(data)

    hertz = data * 1e+9
    kilohertz = data * 1e+6
    megahertz = data * 1000

    return hertz, kilohertz, megahertz


def frequency_converter():
    """
    Handles all frequency conversion
    """
    choice = int(input('''(1) Hertz to ALL
(2) Kilohertz to ALL
(3) Megahertz to ALL
(4) Gigahertz to ALL

Which Sound Frequency conversion would you like to pick: '''))
    print()
    if choice == 1:
        hertz = repeat_input("Hertz: ", "Invalid Number...\n", "float")
        print()

        kilohertz, megahertz, gigahertz = hertz_to_all(hertz)
        print(f'{colors.green}{hertz} in Hertz equals {kilohertz} in Kilohertz.')
        print(f'{hertz} in Hertz equals {megahertz} in Megahertz.')
        print(f'{hertz} in Hertz equals {gigahertz} in Gigahertz. {colors.reset}\n')
        restart.restart()

    elif choice == 2:
        kilohertz = repeat_input("Kilohertz: ", "Invalid Number...\n", "float")
        print()

        hertz, megahertz, gigahertz = kilohertz_to_all(kilohertz)
        print(f'{colors.green}{kilohertz} in Kilohertz equals {hertz} in Hertz.')
        print(f'{kilohertz} in Kilohertz equals {megahertz} in Megahertz.')
        print(f'{kilohertz} in Kilohertz equals {gigahertz} in Gigahertz. {colors.reset}\n')
        restart.restart()

    elif choice == 3:
        megahertz = repeat_input("Megahertz: ", "Invalid Number...\n", "float")
        print()

        hertz, kilohertz, gigahertz = megahertz_to_all(megahertz)
        print(f'{colors.green}{megahertz} in Megahertz equals {hertz} in Hertz.')
        print(f'{megahertz} in Megahertz equals {kilohertz} in Kilohertz.')
        print(f'{megahertz} in Megahertz equals {gigahertz} in Gigahertz. {colors.reset}\n')
        restart.restart()

    elif choice == 4:
        gigahertz = repeat_input("Gigahertz: ", "Invalid Number...\n", "float")
        print()

        hertz, kilohertz, megahertz = gigahertz_to_all(gigahertz)
        print(f'{colors.green}{gigahertz} in Gigahertz equals {hertz} in Hertz.')
        print(f'{gigahertz} in Gigahertz equals {kilohertz} in Kilohertz.')
        print(f'{gigahertz} in Gigahertz equals {megahertz} in Megahertz. {colors.reset}\n')
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        frequency_converter()


def file_converter():
    choice = int(input('''(1) Word Document to PDF
(2) MP4 Video to MP3 Audio

Which File convertion would you like to pick: '''))
    print()
    if choice == 1:
        path = str(input('Enter the file path from which the Word Document is located: '))
        print()
        convert(path)
        time.sleep(1)
        print(colors.green, 'Word to PDF conversion completed! The .pdf file should be found in the same directory '
                            'from where the Word Document was located.\n', colors.reset)
        time.sleep(1)
        restart.restart()
    elif choice == 2:
        mp4_file_path = str(input('Enter the file path from which the MP4 Video is located ('
                                  'C:\Folder\YourName\Desktop\example.mp4): '))
        mp3_file_path = str(input('Output MP3 Audio to where (example - C:\Folder\YourName\Desktop\example.mp3): '))
        video_clip = VideoFileClip(mp4_file_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file_path)
        audio_clip.close()
        video_clip.close()
        print()
        print(colors.green + "Conversion completed!\n", colors.reset)
        time.sleep(1)

        choice = str(input('Want to open the .mp3 file to give it a listen (yes / no): '))
        print()

        if choice.lower() == 'y' or choice.lower() == 'yes':
            os.startfile(mp3_file_path)
            print(colors.green + 'Audio should now be opened and playing!\n', colors.reset)
            restart.restart()
        elif choice.lower() == 'n' or choice.lower() == 'no':
            print(colors.yellow + 'Audio playback skipped...\n', colors.reset)
            restart.restart()
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)
            restart.restart()
    else:
        print(colors.red + "User input error found...\n", colors.reset)
        time.sleep(2)
        file_converter()


def binary_converter():
    choice = int(input("""(1) Binary to Decimal
(2) Decimal to Binary
(3) Binary to Sound

Which Binary conversion would you like to use: """))
    print()
    binary = ""
    if choice == 1:
        number = int(input("Enter your whole decimal number (integer): "))
        print()
        while number > 1:
            binary = str(number % 2) + binary
            number //= 2
        binary = str(number % 2) + binary
        print(colors.green, 'Result:', binary, '\n', colors.reset)
        restart.restart()
    elif choice == 2:
        total = 0
        number = (input("Enter your whole binary number: "))
        print()
        for i in range(1, (number.__len__()) + 1):
            if number[-i] == str(1):
                total = total + (2 ** (i - 1))
        print(colors.green, 'Result:', total, '\n', colors.reset)
        restart.restart()
    elif choice == 3:
        binary = input("Binary input: ")
        print()
        for i in binary:
            if i == "0":
                if windows:
                    winsound.Beep(2000, 100)
                print(colors.green + 'Sound played!\n', colors.reset)
                restart.restart()
            elif i == "1":
                if windows:
                    winsound.Beep(4000, 100)
                print(colors.green + 'Sound played!\n', colors.reset)
                restart.restart()
            else:
                print(colors.red + "User input error found... Please only use 0 or 1 as an input choice...\n",
                      colors.reset)
                time.sleep(2)
                binary_converter()
    else:
        print(colors.red + 'User input error found...\n', colors.reset)
        time.sleep(2)
        binary_converter()


def start():
    print(colors.green + "All Converters", colors.reset)
    choice = int(input('''
(1) Temperature        |       (6) Crypto            |       (11) Angle         |       (16) Binary
(2) Mass               |       (7) Speed             |       (12) Energy        |       (17) Restart 
(3) Length             |       (8) Digital Storage   |       (13) Fuel Economy  |       (18) Quit
(4) Volume             |       (9) Time              |       (14) Sounds
(5) Currency           |       (10) Pressure         |       (15) Files     

Which conversion would you like to use: '''))
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
        print("""To Use The Currency Conversion an API Key is Required
Visit www.currencyconverterapi.com And Follow The Steps To Get an API Key.\n""")
        key = input("API Key: ")

        if validate_key(key):
            currency_converter()
        else:
            print("Invalid Key")
            start()

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
        file_converter()
    elif choice == 16:
        binary_converter()
    elif choice == 17:
        restart.restart()
    elif choice == 18:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        time.sleep(2)
        start()


if __name__ == '__main__':
    start()

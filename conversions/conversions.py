try:
    import winsound
    windows = True
except ImportError:
    linux = True

from docx2pdf import convert
from moviepy.editor import *
from modules import colors
from modules.currency_api import get_currency, validate_key
from modules.tools import repeat_input
from modules.errors import Exit
from time import sleep
import json


def currency_converter():
    """
Handles all currency conversions by using an api key since currencies change their rates frequently
    """
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
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)


# All Crypto-Currency Formulas
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
Handles all crypto conversions and displays the results
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

    elif user_choice == 2:
        ethereum = repeat_input("Ethereum Amount: ", "Invalid Number...\n", "float")
        print()
        bitcoin, dogecoin, shiba_inu = ethereum_to_all(ethereum)
        print(f'{colors.green}{ethereum} in Ethereum equals {bitcoin} in Bitcoin.')
        print(f'{ethereum} in Ethereum equals {dogecoin} in DogeCoin.')
        print(f'{ethereum} in Ethereum equals {shiba_inu} in SHIBA INU. {colors.reset}\n')

    elif user_choice == 3:
        dogecoin = repeat_input("DogeCoin Amount: ", "Invalid Number...\n", "float")
        print()
        bitcoin, ethereum, shiba_inu = bitcoin_to_all(dogecoin)
        print(f'{colors.green}{dogecoin} in DogeCoin equals {bitcoin} in Bitcoin.')
        print(f'{dogecoin} in DogeCoin equals {ethereum} in Ethereum.')
        print(f'{dogecoin} in DogeCoin equals {shiba_inu} in SHIBA INU. {colors.reset}\n')

    elif user_choice == 4:
        shiba_inu = float(input("SHIBA INU Amount: "))
        print()
        bitcoin, ethereum, dogecoin = shiba_inu_to_all(shiba_inu)
        print(f'{colors.green}{shiba_inu} in DogeCoin equals {bitcoin} in Bitcoin.')
        print(f'{shiba_inu} in DogeCoin equals {ethereum} in Ethereum.')
        print(f'{shiba_inu} in DogeCoin equals {dogecoin} in DogeCoin. {colors.reset}\n')
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)


def file_converter():
    """
Handles all file conversions
    """
    choice = int(input('''(1) Word Document to PDF
(2) MP4 Video to MP3 Audio

Which File convertion would you like to pick: '''))
    print()
    if choice == 1:
        path = str(input('Enter the file path from which the Word Document is located: '))
        print()
        convert(path)
        print(colors.green, 'Word to PDF conversion completed! The .pdf file should be found in the same directory '
                            'from where the Word Document was located.\n', colors.reset)
    elif choice == 2:
        # These are raw strings so the backslashes aren't interpreted as escape sequences
        mp4_file_path = str(input(r'Enter the file path from which the MP4 Video is located ('
                                  r'C:\Folder\YourName\Desktop\example.mp4): '))
        mp3_file_path = str(input(r'Output MP3 Audio to where (example - C:\Folder\YourName\Desktop\example.mp3): '))
        video_clip = VideoFileClip(mp4_file_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file_path)
        audio_clip.close()
        video_clip.close()
        print()
        print(colors.green + "Conversion completed!\n", colors.reset)
        choice = repeat_input('Want to open the .mp3 file to give it a listen (yes / no): ',
                              'User input error found',
                              'yes_no'
                              ).lower()

        if choice == 'y' or choice == 'yes':
            os.startfile(mp3_file_path)
            print(colors.green + 'Audio should now be opened and playing!\n', colors.reset)
        elif choice == 'n' or choice == 'no':
            print(colors.yellow + 'Audio playback skipped...\n', colors.reset)
    else:
        print(colors.red + "User input error found...\n", colors.reset)


def binary_converter():
    """
Handles all binary conversions
    """
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
    elif choice == 2:
        total = 0
        number = (input("Enter your whole binary number: "))
        print()
        for i in range(1, (number.__len__()) + 1):
            if number[-i] == str(1):
                total = total + (2 ** (i - 1))
        print(colors.green, 'Result:', total, '\n', colors.reset)
    elif choice == 3:
        binary = input("Binary input: ")
        print()
        for i in binary:
            if i == "0":
                if windows:
                    winsound.Beep(2000, 100)
                print(colors.green + 'Sound played!\n', colors.reset)
            elif i == "1":
                if windows:
                    winsound.Beep(4000, 100)
                print(colors.green + 'Sound played!\n', colors.reset)
            else:
                print(colors.red + "User input error found... Please only use 0 or 1 as an input choice...\n",
                      colors.reset)
                sleep(2)
    else:
        print(colors.red + 'User input error found...\n', colors.reset)


def unit_converter():
    """
Handles all unit conversions with sorted criteria of units to convert from and to
    """
    # This lists all types of units as keys
    # To dictionaries with each unit abbreviation as keys
    # To 2 or 3 item tuples of the full name of the unit AND
    # the ratio between it and the first item in the tuple (x : 1) AND
    # OPTIONALLY an amount to add afterwards (only needed for temperatures currently)
    #
    # All strings should be lowercase, and are formatted correctly in code
    # All unit names should be plural
    # The first unit should be the smallest one, such that all conversion ratios are >= 1
    # In order to minimise floating point errors
    # TODO: Have singular unit names and convert as necessary in code (Not as easy as adding 's' e.g. foot -> feet)
    #
    # Adding to this dictionary is all that is necessary to add units and types of units
    # Adhering to the formatting is highly suggested to keep it readable
    units = {
        'mass': {
            'g': ('grams', 1),
            'kg': ('kilograms', 1000),
            'lb': ('pounds', 453.5924),
            'oz': ('ounces', 28.349526),
        },
        'length': {
            'cm': ('centimeters', 1),
            'm': ('meters', 100),
            'km': ('kilometers', 100000),
            'mi': ('miles', 160934.4),
            'ft': ('feet', 30.48),
            'in': ('inches', 2.54),
        },
        'temperature': {
            'f': ('fahrenheit', 1, 0),
            'c': ('celsius', 1.8, 32),
            'k': ('kelvin', 1.8, -459.667),
            'r': ('rankine', 1, -459.667)
        },
        'volume': {
            'ml': ('milliliters', 1),
            'l': ('liters', 1000),
            'gal': ('gallons', 3785.4),
            'qt': ('quarts', 946.35),
            'pt': ('pints', 473.175),
            'fl oz': ('fluid ounces', 29.57344),
        },
        'speed': {
            'kph': ('kilometers per hour', 1),
            'mph': ('miles per hour', 1.609344),
            'fps': ('feet per second', 1.09728),
            'mps': ('meters per second', 3.6),
            'kn': ('knots', 1.852001),
        },
        'storage': {
            'bit': ('bits', 1),
            'nb': ('nibbles', 4),
            'b': ('bytes', 8),
            'kb': ('kilobytes', 8000),
            'mb': ('megabytes', 8000000),
            'gb': ('gigabytes', 8000000000),
            'kib': ('kibibytes', 8192),
            'meb': ('mebibytes', 8388608),
            'gib': ('gibibytes', 8589935000),
        },
        'time': {
            's': ('seconds', 1),
            'min': ('minutes', 60),
            'h': ('hours', 3600),
            'd': ('days', 86400),
            'w': ('weeks', 604800),
            'fn': ('fornights', 1209600),
            'mon': ('months', 2629800),
            'y': ('years', 31557600),
        },
        'pressure': {
            'pa': ('pascals', 1),
            'kpa': ('kilopascals', 1000),
            'bar': ('bars', 100000),
            'atm': ('atmospheres', 101325),
            'psi': ('pounds per square inch', 14.69595),
        },
        'angle': {
            'arcsec': ('arcseconds', 1),
            'deg': ('degrees', 3600),
            'rad': ('radians', 206264.8),
            'grad': ('gradians', 3240),
            'arcmin': ('arcminutes', 60),
        },
        'energy': {
            'j': ('joules', 1),
            'kj': ('kilojoules', 1000),
            'wh': ('watt hours', 3600),
            'kwh': ('kilowatt hours', 3600000),
            'cal': ('calories', 4.184),
            'kcal': ('kilocalories', 4184),
        },
        'fuel economy': {
            'mpg': ('miles per gallon', 1),
            'mpgi': ('miles per gallon imperial', 1.2),
            'kpl': ('kilometers per liter', 2.82428),
        },
    }

    unit_type = repeat_input('What type of unit do you want to convert?\n    ' +
                             '\n    '.join(f'({ind}) {unit_name.title()}' for ind, unit_name in
                                           enumerate(units, start=1)) +
                             '\nSelect a number: ',
                             'Select a valid number',
                             'int',
                             lambda i: 0 < int(i) <= len(units)
                             )
    conversion_table = units[list(units)[int(unit_type) - 1]]
    unit_names = list(f'{name.title()} ({abbr})' for abbr, (name, *_) in conversion_table.items())
    input_unit = repeat_input('Which unit are you converting from?\n    ' +
                              f'\n    '.join(unit_names) +
                              '\nSelect an abbreviation: ',
                              'Select a valid abbreviation',
                              custom_validation=lambda i: i.lower() in conversion_table
                              ).lower()
    input_amount = float(repeat_input('What value are you converting? ',
                                      'Input a valid number',
                                      'float'
                                      ))
    output_unit = repeat_input('Which unit are you converting to?\n    ' +
                               f'\n    '.join(unit_names + ['All Units (all)']) +
                               '\nSelect an abbreviation: ',
                               'Select a valid abbreviation',
                               custom_validation=lambda i: i.lower() in conversion_table or i.lower() == 'all'
                               ).lower()
    print()

    if len(conversion_table[input_unit]) == 2:
        _, input_ratio = conversion_table[input_unit]
        input_offset = 0
    else:
        _, input_ratio, input_offset = conversion_table[input_unit]
    true_amount = input_amount * input_ratio + input_offset

    if output_unit != 'all':
        if len(conversion_table[output_unit]) == 2:
            _, output_ratio = conversion_table[output_unit]
            output_offset = 0
        else:
            _, output_ratio, output_offset = conversion_table[output_unit]
        print(f'{(true_amount - output_offset) / output_ratio:.3f} {output_unit}')
    else:
        for unit, (_, *output_values) in conversion_table.items():
            if unit == input_unit:
                continue

            if len(output_values) == 1:
                output_ratio, = output_values
                output_offset = 0
            else:
                output_ratio, output_offset = output_values
            print(f'{(true_amount - output_offset) / output_ratio:.3f} {unit}')
    print()


def start():
    """
Main hub UI for all of the converters used in the project
    """
    while True:
        print(colors.green + "All Converters\n", colors.reset)
        choice = int(input('''(1) Units
(2) Currency
(3) Crypto
(4) Files
(5) Binary
(6) Restart
(7) Quit

Which conversion would you like to use: '''))
        print()
        if choice == 1:
            unit_converter()
        elif choice == 2:
            print("""To Use The Currency Conversion an API Key is Required
Visit www.currencyconverterapi.com And Follow The Steps To Get an API Key.\n""")
            key = input("API Key: ")
            if validate_key(key):
                currency_converter()
            else:
                print("Invalid Key")
        elif choice == 3:
            crypto_converter()
        elif choice == 4:
            file_converter()
        elif choice == 5:
            binary_converter()
        elif choice == 6:
            break
        elif choice == 7:
            raise Exit
        else:
            print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)


if __name__ == '__main__':
    start()

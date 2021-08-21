try:
    import winsound
    windows = True
    linux = False
except ImportError:
    # Do not import winsound here as it will cause an error for linux and MacOs users.
    linux = True
    windows = False

from modules import colors, currency_api
from modules.tools import repeat_input
from modules.errors import Exit
import time


def currency_converter():
    """
Handles all currency conversions by using an api key since currencies change their rates frequently
    """
    api_key = currency_api.get_api_key()
    currency_1 = None
    currency_2 = None
    currencies = {currency['id']: currency['currencyName'] for currency in currency_api.get_currencies(api_key)}
    while True:
        choice = int(input('''(1) Select currency to convert from
(2) Select currency to convert to
(3) List available currencies
(4) Get exchange rate
(5) Convert amount
(6) Return to list of converters
(7) Exit

Which Currency option would you like to use: '''))
        print()

        if choice == 1:
            currency_1 = repeat_input('Which currency are you converting from? Input the currency code: ',
                                      'Not a currency code',
                                      custom_validation=lambda i: i in currencies)
        elif choice == 2:
            currency_2 = repeat_input('Which currency are you converting to? Input the currency code: ',
                                      'Not a currency code',
                                      custom_validation=lambda i: i in currencies)
        elif choice == 3:
            print('Available currencies: ')
            for abbreviation, name in currencies.items():
                print(f'{name: <30} ({abbreviation})')
        elif choice == 4:
            if currency_1 is None or currency_2 is None:
                print('You have not selected a currency to convert to or from')
            else:
                print(f'The exchange rate is {currency_api.get_currency(currency_1, currency_2, api_key)}')
        elif choice == 5:
            amount = float(repeat_input('How much are you converting? ', 'Not a valid number', 'float'))
            rate = currency_api.get_currency(currency_1, currency_2, api_key)
            print(f'{amount} {currency_1} = {amount * rate} {currency_2}')
        elif choice == 6:
            break
        elif choice == 7:
            raise Exit
        else:
            print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
            time.sleep(2)


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
    while True:
        choice = int(
            input("""(1) Bitcoin to ALL
(2) Ethereum to ALL
(3) DogeCoin  to ALL
(4) SHIBA INU to ALL
(5) Return to list of converters
(6) Exit
    
Select a crypto conversion: """))
        print()
        if choice == 1:
            bitcoin = repeat_input("Bitcoin Amount: ", "Invalid Number...\n", "float")
            print()
            ethereum, dogecoin, shiba_inu = bitcoin_to_all(bitcoin)
            print(f'{colors.green}{bitcoin} in Bitcoin equals {ethereum} in Ethereum.')
            print(f'{bitcoin} in Bitcoin equals {dogecoin} in DogeCoin.')
            print(f'{bitcoin} in Bitcoin equals {shiba_inu} in SHIBA INU. {colors.reset}\n')
        elif choice == 2:
            ethereum = repeat_input("Ethereum Amount: ", "Invalid Number...\n", "float")
            print()
            bitcoin, dogecoin, shiba_inu = ethereum_to_all(ethereum)
            print(f'{colors.green}{ethereum} in Ethereum equals {bitcoin} in Bitcoin.')
            print(f'{ethereum} in Ethereum equals {dogecoin} in DogeCoin.')
            print(f'{ethereum} in Ethereum equals {shiba_inu} in SHIBA INU. {colors.reset}\n')
        elif choice == 3:
            dogecoin = repeat_input("DogeCoin Amount: ", "Invalid Number...\n", "float")
            print()
            bitcoin, ethereum, shiba_inu = bitcoin_to_all(dogecoin)
            print(f'{colors.green}{dogecoin} in DogeCoin equals {bitcoin} in Bitcoin.')
            print(f'{dogecoin} in DogeCoin equals {ethereum} in Ethereum.')
            print(f'{dogecoin} in DogeCoin equals {shiba_inu} in SHIBA INU. {colors.reset}\n')
        elif choice == 4:
            shiba_inu = float(input("SHIBA INU Amount: "))
            print()
            bitcoin, ethereum, dogecoin = shiba_inu_to_all(shiba_inu)
            print(f'{colors.green}{shiba_inu} in DogeCoin equals {bitcoin} in Bitcoin.')
            print(f'{shiba_inu} in DogeCoin equals {ethereum} in Ethereum.')
            print(f'{shiba_inu} in DogeCoin equals {dogecoin} in DogeCoin. {colors.reset}\n')
        elif choice == 5:
            break
        elif choice == 6:
            raise Exit
        else:
            print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
            time.sleep(2)


def binary_converter():
    """
Converts binary to sound
    """
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
            time.sleep(2)


def unit_converter():
    """
Handles all unit conversions with sorted criteria of units to convert from and to
    """
    units = {
        'Mass': {
            'g': ('grams', 1),
            'kg': ('kilograms', 1000),
            'lb': ('pounds', 453.5924),
            'oz': ('ounces', 28.349526),
        },
        'Length': {
            'cm': ('centimeters', 1),
            'm': ('meters', 100),
            'km': ('kilometers', 100000),
            'mi': ('miles', 160934.4),
            'ft': ('feet', 30.48),
            'in': ('inches', 2.54),
        },
        'Temperature': {
            'f': ('fahrenheit', 1, 0),
            'c': ('celsius', 1.8, 32),
            'k': ('kelvin', 1.8, -459.667),
            'r': ('rankine', 1, -459.667)
        },
        'Volume': {
            'ml': ('milliliters', 1),
            'l': ('liters', 1000),
            'gal': ('gallons', 3785.4),
            'qt': ('quarts', 946.35),
            'pt': ('pints', 473.175),
            'fl oz': ('fluid ounces', 29.57344),
        },
        'Speed': {
            'kph': ('kilometers per hour', 1),
            'mph': ('miles per hour', 1.609344),
            'fps': ('feet per second', 1.09728),
            'mps': ('meters per second', 3.6),
            'kn': ('knots', 1.852001),
        },
        'Storage': {
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
        'Time': {
            's': ('seconds', 1),
            'min': ('minutes', 60),
            'h': ('hours', 3600),
            'd': ('days', 86400),
            'w': ('weeks', 604800),
            'fn': ('fornights', 1209600),
            'mon': ('months', 2629800),
            'y': ('years', 31557600),
        },
        'Pressure': {
            'pa': ('pascals', 1),
            'kpa': ('kilopascals', 1000),
            'bar': ('bars', 100000),
            'atm': ('atmospheres', 101325),
            'psi': ('pounds per square inch', 14.69595),
        },
        'Angle': {
            'arcsec': ('arcseconds', 1),
            'deg': ('degrees', 3600),
            'rad': ('radians', 206264.8),
            'grad': ('gradians', 3240),
            'arcmin': ('arcminutes', 60),
        },
        'Energy': {
            'j': ('joules', 1),
            'kj': ('kilojoules', 1000),
            'wh': ('watt hours', 3600),
            'kwh': ('kilowatt hours', 3600000),
            'cal': ('calories', 4.184),
            'kcal': ('kilocalories', 4184),
        },
        'Fuel Economy\n': {
            'mpg': ('miles per gallon', 1),
            'mpgi': ('miles per gallon imperial', 1.2),
            'kpl': ('kilometers per liter', 2.82428),
        },
    }

    unit_type = repeat_input('What unit do you want to convert from.\n\n' +
                             '\n'.join(f'({ind}) {unit_name.title()}' for ind, unit_name in
                                       enumerate(units, start=1)) +
                             '\nSelect a number: ',
                             '\nSelect a valid number!',
                             'int',
                             lambda i: 0 < int(i) <= len(units)
                             )
    print()
    conversion_table = units[list(units)[int(unit_type) - 1]]
    unit_names = [
        f'{name.title()} ({abbr})'
        for abbr, (name, *_) in conversion_table.items()
    ]

    input_unit = repeat_input('Which unit are you converting from.\n\n' +
                              f'\n'.join(unit_names) +
                              '\n\nSelect an abbreviation: ',
                              '\nSelect a valid abbreviation!',
                              custom_validation=lambda i: i.lower() in conversion_table
                              ).lower()
    print()
    input_amount = float(repeat_input('What value are you converting: ',
                                      '\nInput a valid number!',
                                      'float'
                                      ))
    print()
    output_unit = repeat_input('Which unit are you converting to. ' +
                               f'\n'.join(unit_names + ['All Units (all)']) +
                               '\n\nSelect an abbreviation: ',
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


def convert_to_base_10(number: str, base: int, alphabet: str) -> int:
    try:
        integer_part, decimal_part = number.split('.')
    except ValueError:
        # No decimal place - integer
        integer_part = number
        decimal_part = ''

    base_place_values = [1]
    for _ in range(max(len(integer_part), len(decimal_part))):
        base_place_values.append(base_place_values[-1] * base)

    base_ten_number = sum(alphabet.index(digit) * base_place_values[len(integer_part) - index]
                          for index, digit in enumerate(integer_part, start=1))

    base_ten_number += sum(map(lambda i: 1 / i, filter(lambda i: i != 0,
                                                       (int(digit) * base_place_values[index]
                                                        for index, digit in enumerate(decimal_part, start=1))
                                                       )))

    return base_ten_number


def convert_from_base_10(number: int, target_base: int, alphabet: str) -> str:
    """
Used as a formula to convert from bases of 10
    """
    output_number = []

    while number > 0:
        output_number.append(alphabet[number % target_base])
        number //= target_base

    return ''.join(reversed(output_number))


def base_converter():
    """
Converts between bases and numbers
    """
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    input_base = 10
    output_base = 10
    while True:
        choice = int(input('''(1) Specify input base
(2) Specify output base
(3) Swap input and output bases
(4) Define alphabet (must be done for bases > 62)
(5) Convert number
(6) Return to list of converters
(7) Exit
    
Select a Base Converter choice: '''))
        print()

        if choice == 1:
            input_base = int(repeat_input('What base are you converting from? ',
                                          'Base must be greater than 0',
                                          'int',
                                          lambda i: int(i) > 0))
        elif choice == 2:
            output_base = int(repeat_input('What base are you converting to? ',
                                           'Base must be greater than 0',
                                           'int',
                                           lambda i: int(i) > 0))
        elif choice == 3:
            input_base, output_base = output_base, input_base
        elif choice == 4:
            alphabet = input('Alphabet: ')
        elif choice == 5:
            number = input('What number are you converting? ')
            try:
                base_10 = convert_to_base_10(number, input_base, alphabet)
                print(convert_from_base_10(base_10, output_base, alphabet))
            except (IndexError, ValueError):
                # Character encountered that isn't in the alphabet provided
                print(colors.red + 'Character found not in the alphabet. Define a new alphabet and try again...\n',
                      colors.reset)
        elif choice == 6:
            break
        elif choice == 7:
            raise Exit
        else:
            print(colors.red + 'Invalid choice...\n', colors.reset)
            time.sleep(2)


def start():
    """
Main hub UI for all of the converters used in the project
    """
    while True:
        print(colors.green + "All Converters\n", colors.reset)
        choice = int(input('''(1) Units
(2) Currency
(3) Crypto
(4) Binary to Sound
(5) Base Converter
(6) Restart
(7) Quit

Which conversion would you like to use: '''))
        print()
        if choice == 1:
            unit_converter()
        elif choice == 2:
            currency_converter()
        elif choice == 3:
            crypto_converter()
        elif choice == 4:
            binary_converter()
        elif choice == 5:
            base_converter()
        elif choice == 6:
            break
        elif choice == 7:
            raise Exit
        else:
            print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)


if __name__ == '__main__':
    start()

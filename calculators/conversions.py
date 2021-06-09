import colors
import end
import restart
import time
from currency_api import get_currency


def currency_converter():
    user_choice = int(
        input("""(1) US Dollar to ALL
(2) Euro to ALL
(3) Canadian Dollar to ALL
(4) Japanese Yen to ALL
(5) Moroccan MAD to ALL
Select a currency conversion:    """))
    print()
    if user_choice == 1:
        user_dollar = float(input("Dollar Amount: "))
        print()
        d_to_e = float(user_dollar * get_currency("USD_EUR"))
        d_to_j = float(user_dollar * get_currency("USD_JPY"))
        d_to_c = float(user_dollar * get_currency("USD_CAD"))
        d_to_mad = float(user_dollar * get_currency("USD_MAD"))
        print(colors.green, user_dollar, "in US Dollar equals",
              d_to_e, "in Euros.", colors.reset)
        print(colors.green, user_dollar, "in US Dollar equals",
              d_to_j, "in Japanese Yen.", colors.reset)
        print(colors.green, user_dollar, "in US Dollar equals",
              d_to_c, "in Canadian Dollar.", colors.reset)
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
              e_to_d, "in US Dollars.", colors.reset)
        print(colors.green, user_euro, "in Euro equals",
              e_to_j, "in Japanese Yen.", colors.reset)
        print(colors.green, user_euro, "in Euro equals",
              e_to_c, "in Canadian Dollar.", colors.reset)
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
              c_to_d, "in US Dollars.", colors.reset)
        print(colors.green, user_canadian, "in Canadian Dollar equals",
              c_to_j, "in Japanese Yen.", colors.reset)
        print(colors.green, user_canadian, "in Canadian Dollar equals",
              c_to_e, "in Euro.", colors.reset)
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
              y_to_d, "in US Dollars.", colors.reset)
        print(colors.green, user_yen, "in Japanese Yen equals",
              y_to_e, "in Euros.", colors.reset)
        print(colors.green, user_yen, "in Japanese Yen equals",
              y_to_c, "in Canadian Dollar.", colors.reset)
        print(colors.green, user_yen, "in Japanese Yen equals",
              y_to_mad, "in Moroccan MAD.\n", colors.reset)
        restart.restart()
    elif user_choice == 5:
        user_mad = float(input("Moroccan MAD Amount: "))
        print()
        mad_to_d = float(user_mad * get_currency("MAD_USD"))
        mad_to_e = float(user_mad * get_currency("MAD_EUR"))
        mad_to_c = float(user_mad * get_currency("MAD_CAD"))
        mad_to_yen = float(user_mad * get_currency("MAD_JPY"))
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_d, "in US Dollars.", colors.reset)
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_e, "in Euros.", colors.reset)
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_c, "in Canadian Dollar.", colors.reset)
        print(colors.green, user_mad, "in Moroccan MAD equals",
              mad_to_yen, "in Japanese Yen.\n", colors.reset)
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        currency_converter()


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
        user_celsius = float(input("Celsius: "))
        print()
        c_to_f = float(user_celsius * 1.8 + 32)
        c_to_k = float(user_celsius + 273.15)
        print(colors.green, user_celsius, "in Celsius equals",
              c_to_f, "in Fahrenheit.", colors.reset)
        print(colors.green, user_celsius, "in Celsius equals",
              c_to_k, "in Kelvin.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        user_fahrenheit = float(input("Fahrenheit: "))
        print()
        f_to_c = float((user_fahrenheit - 32) * 5 / 9)
        f_to_k = float((user_fahrenheit - 32) * 5 / 9 + 273.15)
        print(colors.green, user_fahrenheit, "in Fahrenheit equals",
              f_to_c, "in Celsius.", colors.reset)
        print(colors.green, user_fahrenheit, "in Fahrenheit equals",
              f_to_k, "in Kelvin.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        user_kelvin = float(input("Kelvin: "))
        print()
        k_to_c = float(user_kelvin - 273.15)
        k_to_f = float((user_kelvin - 273.15) * 1.8 + 32)
        print(colors.green, user_kelvin, "in Kelvin equals",
              k_to_c, "in Celsius.", colors.reset)
        print(colors.green, user_kelvin, "in Kelvin equals",
              k_to_f, "in Fahrenheit.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        temp_converter()


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
        user_kilo = float(input("Kilograms: "))
        print()
        kg_to_g = float(user_kilo * 1000)
        kg_to_p = float(user_kilo * 2.205)
        kg_to_o = float(user_kilo * 35.274)
        print(colors.green, user_kilo, "in Kilograms equals",
              kg_to_g, "in Grams.", colors.reset)
        print(colors.green, user_kilo, "in Kilograms equals",
              kg_to_p, "in Pounds.", colors.reset)
        print(colors.green, user_kilo, "in Kilograms equals",
              kg_to_o, "in Ounces.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        user_gram = float(input("Grams: "))
        print()
        g_to_kg = float(user_gram / 1000)
        g_to_p = float(user_gram / 454)
        g_to_o = float(user_gram / 28.35)
        print(colors.green, user_gram, "in Grams equals",
              g_to_kg, "in Kilograms.", colors.reset)
        print(colors.green, user_gram, "in Grams equals",
              g_to_p, "in Pounds.", colors.reset)
        print(colors.green, user_gram, "in Grams equals",
              g_to_o, "in Ounces.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        user_pound = float(input("Pounds: "))
        print()
        p_to_kg = float(user_pound / 2.205)
        p_to_g = float(user_pound * 454)
        p_to_o = float(user_pound * 16)
        print(colors.green, user_pound, "in Pounds equals",
              p_to_kg, "in Kilograms.", colors.reset)
        print(colors.green, user_pound, "in Pounds equals",
              p_to_g, "in Grams.", colors.reset)
        print(colors.green, user_pound, "in Pounds equals",
              p_to_o, "in Ounces.\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        user_ounce = float(input("Ounces: "))
        print()
        o_to_kg = float(user_ounce / 35.274)
        o_to_g = float(user_ounce * 28.35)
        o_to_p = float(user_ounce / 16)
        print(colors.green, user_ounce, "in Ounces equals",
              o_to_kg, "in Kilograms.", colors.reset)
        print(colors.green, user_ounce, "in Ounces equals",
              o_to_g, "in Grams.", colors.reset)
        print(colors.green, user_ounce, "in Ounces equals",
              o_to_p, "in Pounds.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        mass_converter()


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
        ft = float(input("Feet: "))
        print()
        ft_to_inch = ft * 12
        ft_to_yard = ft / 3
        ft_to_mile = ft / 5280
        print(colors.green, ft, "in Feet equals",
              ft_to_inch, "in Inches.", colors.reset)
        print(colors.green, ft, "in Feet equals",
              ft_to_yard, "in Yards.", colors.reset)
        print(colors.green, ft, "in Feet equals",
              ft_to_mile, "in Miles.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        inch = float(input("Inches: "))
        print()
        inch_to_ft = inch / 12
        inch_to_yard = inch / 36
        inch_to_mile = inch / 63360
        print(colors.green, inch, "in Inches equals",
              inch_to_ft, "in Feet.", colors.reset)
        print(colors.green, inch, "in Inches equals",
              inch_to_yard, "in Yards.", colors.reset)
        print(colors.green, inch, "in Inches equals",
              inch_to_mile, "in Miles.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        yard = float(input("Yards: "))
        print()
        yard_to_inch = yard * 36
        yard_to_foot = yard * 3
        yard_to_mile = yard / 1760
        print(colors.green, yard, "in Yards equals",
              yard_to_inch, "in Inches.", colors.reset)
        print(colors.green, yard, "in Yards equals",
              yard_to_foot, "in Feet.", colors.reset)
        print(colors.green, yard, "in Yards equals",
              yard_to_mile, "in Miles.\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        mile = float(input("Miles: "))
        print()
        mile_to_inch = mile * 63360
        mile_to_foot = mile * 5280
        mile_to_yard = mile * 1760
        print(colors.green, mile, "in Miles equals",
              mile_to_inch, "in Inches.", colors.reset)
        print(colors.green, mile, "in Miles equals",
              mile_to_foot, "in Feet.", colors.reset)
        print(colors.green, mile, "in Miles equals",
              mile_to_yard, "in Yards.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        length_converter()


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
        ml = float(input("Milliliters: "))
        print()
        ml_to_l = ml * (1 / 1000)
        print(colors.green, ml, "in Milliliters equals",
              ml_to_l, "in Liters.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        l = float(input("Liters: "))
        print()
        l_to_ml = l * (1000 / 1)
        print(colors.green, l, "in Liters equals",
              l_to_ml, "in Milliliters.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        gallon = float(input("Gallons: "))
        print()
        gallon_to_quart = gallon * 4
        gallon_to_pint = gallon * 8
        gallon_to_ounce = gallon * 128
        print(colors.green, gallon, "in Gallons equals",
              gallon_to_quart, "in Quart.", colors.reset)
        print(colors.green, gallon, "in Gallons equals",
              gallon_to_pint, "in Pint.", colors.reset)
        print(colors.green, gallon, "in Gallons equals",
              gallon_to_ounce, "in Ounces.\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        quart = float(input("Quarts: "))
        print()
        quart_to_gallon = quart / 4
        quart_to_pint = quart * 2
        quart_to_ounce = quart * 32
        print(colors.green, quart, "in Ounces equals",
              quart_to_gallon, "in Gallons.", colors.reset)
        print(colors.green, quart, "in Ounces equals",
              quart_to_pint, "in Pints.", colors.reset)
        print(colors.green, quart, "in Ounces equals",
              quart_to_ounce, "in Ounces.\n", colors.reset)
        restart.restart()
    elif user_choice == 5:
        pint = float(input("Pints: "))
        print()
        pint_to_gallon = pint / 8
        pint_to_quart = pint / 2
        pint_to_ounce = pint * 16
        print(colors.green, pint, "in Pints equals",
              pint_to_gallon, "in Gallons.", colors.reset)
        print(colors.green, pint, "in Pints equals",
              pint_to_quart, "in Quarts.", colors.reset)
        print(colors.green, pint, "in Pints equals",
              pint_to_ounce, "in Ounces.\n", colors.reset)
        restart.restart()
    elif user_choice == 6:
        ounce = float(input("Ounces: "))
        print()
        ounce_to_quart = ounce / 32
        ounce_to_gallon = ounce / 128
        ounce_to_pint = ounce / 16
        print(colors.green, ounce, "in Ounces equals",
              ounce_to_quart, "in Quarts.", colors.reset)
        print(colors.green, ounce, "in Ounces equals",
              ounce_to_gallon, "in Gallons.", colors.reset)
        print(colors.green, ounce, "in Ounces equals",
              ounce_to_pint, "in Pints.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
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
              btc_to_e, "in Ethereum.", colors.reset)
        print(colors.green, btc, "in Bitcoin equals",
              btc_to_dc, "in DogeCoin.", colors.reset)
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
              e_to_b, "in Bitcoin.", colors.reset)
        print(colors.green, eth, "in Ethereum equals",
              e_to_dc, "in DogeCoin.", colors.reset)
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
              dc_to_b, "in Bitcoin.", colors.reset)
        print(colors.green, doge_c, "in DogeCoin equals",
              dc_to_e, "in Ethereum.", colors.reset)
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
              sh_to_b, "in Bitcoin.", colors.reset)
        print(colors.green, sh, "in SHIBA INU equals",
              sh_to_e, "in Ethereum.", colors.reset)
        print(colors.green, sh, "in SHIBA INU equals",
              sh_to_dc, "in DogeCoin.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        crypto_converter()


def mph():
    choice = float(input('How many Miles Per Hour: '))
    print()
    mph_fps = choice * 1.467
    mph_mps = choice / 2.237
    mph_kms = choice * 1.609
    mph_knot = choice / 1.151
    print(colors.green, choice, 'Miles Per Hour equals',
          mph_fps, 'in Foot Per Seconds.', colors.reset)
    print(colors.green, choice, 'Miles Per Hour equals',
          mph_mps, 'in Meters Per Second.', colors.reset)
    print(colors.green, choice, 'Miles Per Hour equals',
          mph_kms, 'in Kilometers Per Hour.', colors.reset)
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
          fps_mph, 'in Miles Per Hour.', colors.reset)
    print(colors.green, choice, 'Foot Per Seconds equals',
          fps_mps, 'in Meters Per Second.', colors.reset)
    print(colors.green, choice, 'Foot Per Seconds equals',
          fps_kph, 'in Kilometers Per Hour.', colors.reset)
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
          mps_mph, 'in Miles Per Hour.', colors.reset)
    print(colors.green, choice, 'Meters Per Second equals',
          mps_fps, 'in Foot Per Second.', colors.reset)
    print(colors.green, choice, 'Meters Per Second equals',
          mps_kph, 'in Kilometers Per Hour.', colors.reset)
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
          kph_mph, 'in Miles Per Hour.', colors.reset)
    print(colors.green, choice, 'Meters Per Second equals',
          kph_fps, 'in Foot Per Second.', colors.reset)
    print(colors.green, choice, 'Meters Per Second equals',
          kph_mps, 'in Meters Per Second.', colors.reset)
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
          knot_mph, 'in Miles Per Hour.', colors.reset)
    print(colors.green, choice, 'Knots equals',
          knot_fps, 'in Foot Per Second.', colors.reset)
    print(colors.green, choice, 'Knots equals', knot_mps,
          'in Meters Per Second.', colors.reset)
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
        time.sleep(1)
        start()


def time_converter():
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
          b_k, 'in Kilobytes.', colors.reset)
    print(colors.green, choice, 'Bytes equals',
          b_m, 'in Megabytes.', colors.reset)
    print(colors.green, choice, 'Bytes equals',
          b_g, 'in Gigabytes.', colors.reset)
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
          k_b, 'in Bytes.', colors.reset)
    print(colors.green, choice, 'Kilobytes equals',
          k_m, 'in Megabytes.', colors.reset)
    print(colors.green, choice, 'Kilobytes equals',
          k_g, 'in Gigabytes.', colors.reset)
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
          m_b, 'in Bytes.', colors.reset)
    print(colors.green, choice, 'Megabytes equals',
          m_k, 'in Kilobytes.', colors.reset)
    print(colors.green, choice, 'Megabytes equals',
          m_g, 'in Gigabytes.', colors.reset)
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
          g_b, 'in Bytes.', colors.reset)
    print(colors.green, choice, 'Gigabytes equals',
          g_k, 'in Kilobytes.', colors.reset)
    print(colors.green, choice, 'Gigabytes equals',
          g_m, 'in Megabytes.', colors.reset)
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
          t_b, 'in Bytes.', colors.reset)
    print(colors.green, choice, 'Terabytes equals',
          t_k, 'in Kilobytes.', colors.reset)
    print(colors.green, choice, 'Terabytes equals',
          t_m, 'in Megabytes.', colors.reset)
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
        time.sleep(1)
        start()


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
              pr_to_kpa, "in kilopascal [kPa].", colors.reset)
        print(colors.green, pressure, "in pascal [Pa] equals",
              pr_to_bar, "in bar.", colors.reset)
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
              kp_to_p, "in pascal [Pa].", colors.reset)
        print(colors.green, pressure, "in kilopascal [kPa] equals",
              kp_to_bar, "in bar.", colors.reset)
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
              bar_to_p, "in pascal [Pa].", colors.reset)
        print(colors.green, pressure, "in bar equals",
              bar_to_kpa, "in kilopascal [kPa].", colors.reset)
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
              atm_to_p, "in pascal [Pa].", colors.reset)
        print(colors.green, pressure, "in Standard atmosphere [atm] equals",
              atm_to_kpa, "in kilopascal [kPa].", colors.reset)
        print(colors.green, pressure, "in Standard atmosphere [atm] equals",
              atm_to_bar, "in bar.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
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
              ang_to_rad, "in Radian [rad].", colors.reset)
        print(colors.green, angle, "in Degree [°] equals",
              ang_to_grad, "in grad [^g].", colors.reset)
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
              ang_to_deg, "in Degree [°].", colors.reset)
        print(colors.green, angle, "in Radian [rad] equals",
              ang_to_grad, "in grad [^g].", colors.reset)
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
              ang_to_deg, "in Degree [°].", colors.reset)
        print(colors.green, angle, "in grad [^g] equals",
              ang_to_rad, "in Radian [rad].", colors.reset)
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
              ang_to_deg, "in Degree [°].", colors.reset)
        print(colors.green, angle, "in Minute ['] equals",
              ang_to_rad, "in Radian [rad].", colors.reset)
        print(colors.green, angle, "in Minute ['] equals",
              ang_to_grad, "in grad [^g].\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        angle_converter()


def energy_converter():
    choice = int(input('''(1) Joule to ALL
(2) KiloJoule to ALL
(3) Watt Hour to ALL
(4) Kilowatt Hour to ALL
Which energy convertion would you like to pick: '''))
    print()
    if choice == 1:
        j = float(input("Joules: "))
        print()
        j_to_kj = float(j / 1000)
        j_to_w = float(j / 3600)
        j_to_kw = float(j / 3.6e+6)
        print(colors.green, j, "in Joules equals",
              j_to_kj, "in Kilojoules.", colors.reset)
        print(colors.green, j, "in Joules equals",
              j_to_w, "in Watts.", colors.reset)
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
              kj_to_j, "in Kilojoules.", colors.reset)
        print(colors.green, kj, "in Kilojoules equals",
              kj_to_w, "in Watts.", colors.reset)
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
              w_to_j, "in Joules.", colors.reset)
        print(colors.green, w, "in Watts equals",
              w_to_kj, "in Kilojoules.", colors.reset)
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
              kw_to_j, "in Joules.", colors.reset)
        print(colors.green, kw, "in Kilowatts equals",
              kw_to_kj, "in Kilojoules.", colors.reset)
        print(colors.green, kw, "in Kilowatts equals",
              kw_to_w, "in Watts.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        angle_converter()


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
(13) Restart
(14) Quit
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
        restart.restart()
    elif choice == 14:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        start()


if __name__ == '__main__':
    start()

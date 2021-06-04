import colors
import end
import restart
import currency_api
import time


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
        d_to_e = float(user_dollar * 0.83)
        d_to_j = float(user_dollar * 103.91)
        d_to_c = float(user_dollar * 1.27)
        d_to_mad = float(user_dollar * 8.82)
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
        e_to_d = float(user_euro * 1.21)
        e_to_j = float(user_euro * 125.49)
        e_to_c = float(user_euro * 1.54)
        e_to_mad = float(user_euro * 10.77)
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
        c_to_d = float(user_canadian * 0.79)
        c_to_j = float(user_canadian * 125.49)
        c_to_e = float(user_canadian * 0.65)
        c_to_mad = float(user_canadian * 7.33)
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
        y_to_d = float(user_yen * 0.0096)
        y_to_e = float(user_yen * 0.0080)
        y_to_c = float(user_yen * 0.012)
        y_to_mad = float(user_yen * 0.08)
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
        mad_to_d = float(user_mad * 0.11)
        mad_to_e = float(user_mad * 0.093)
        mad_to_c = float(user_mad * 0.14)
        mad_to_yen = float(user_mad * 12.42)
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
              btc_to_sh, "B in SHIBA INU.\n", colors.reset)
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
        dc_to_sh = float(doge_c * 43, 745)
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


def wrong_option():
    print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
    start()


INPUT_CHOICES = {
    1: temp_converter,
    2: mass_converter,
    3: length_converter,
    4: volume_converter,
    5: currency_converter,
    6: crypto_converter,
    7: restart.restart,
    8: end.end,
    9: wrong_option
}


def start():
    choice = int(input('''
(1) Temperature Converter
(2) Mass Converter
(3) Length Converter
(4) Volume Converter
(5) Currency Converter
(6) Crypto Converter
(7) Restart
(8) Quit
What converter would you like to perform: '''))
    print()

    # get function from dict and execute
    # if option not found then execute wrong option function
    INPUT_CHOICES.get(choice, 9)()


if __name__ == '__main__':
    start()

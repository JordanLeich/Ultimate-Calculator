import os
import pytube
from pytube import YouTube
import colors
import end
import restart


def currency_converter():
    user_choice = int(
        input("""US Dollar to ALL (1)
            Euro to ALL (2)
            Canadian to ALL (3)
            Japanese Yen (4)
            Select a currency conversion:    """))
    print()
    if user_choice == 1:
        user_dollar = float(input("Dollar Amount: "))
        print()
        d_to_e = float(user_dollar * 0.83)
        d_to_j = float(user_dollar * 103.91)
        d_to_c = float(user_dollar * 1.27)
        print(colors.green, user_dollar, "in US Dollar equals", d_to_e, "in Euros.", colors.reset)
        print(colors.green, user_dollar, "in US Dollar equals", d_to_j, "in Japanese Yen.", colors.reset)
        print(colors.green, user_dollar, "in US Dollar equals", d_to_c, "in Canadian.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        user_euro = float(input("Euro Amount: "))
        print()
        e_to_d = float(user_euro * 1.21)
        e_to_j = float(user_euro * 125.49)
        e_to_c = float(user_euro * 1.54)
        print(colors.green, user_euro, "in Euro equals", e_to_d, "in US Dollars.", colors.reset)
        print(colors.green, user_euro, "in Euro equals", e_to_j, "in Japanese Yen.", colors.reset)
        print(colors.green, user_euro, "in Euro equals", e_to_c, "in Canadian.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        user_canadian = float(input("Canadian Amount: "))
        print()
        c_to_d = float(user_canadian * 0.79)
        c_to_j = float(user_canadian * 125.49)
        c_to_e = float(user_canadian * 0.65)
        print(colors.green, user_canadian, "in Canadian equals", c_to_d, "in US Dollars.", colors.reset)
        print(colors.green, user_canadian, "in Canadian equals", c_to_j, "in Japanese Yen.", colors.reset)
        print(colors.green, user_canadian, "in Canadian equals", c_to_e, "in Euro.\n", colors.reset)
        restart.restart()
    elif user_choice == 4:
        user_yen = float(input("Japanese Yen Amount: "))
        print()
        y_to_d = float(user_yen * 0.0096)
        y_to_e = float(user_yen * 0.0080)
        y_to_c = float(user_yen * 0.012)
        print(colors.green, user_yen, "in Japanese Yen equals", y_to_d, "in US Dollars.", colors.reset)
        print(colors.green, user_yen, "in Japanese Yen equals", y_to_e, "in Euros.", colors.reset)
        print(colors.green, user_yen, "in Japanese Yen equals", y_to_c, "in Canadian.\n", colors.reset)
        restart.restart()
    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        start()


def youtube_converter():
    video_url = input('Enter YouTube video URL: ')
    print()
    print(colors.green + 'Video is downloaded, please check your current directory to find the file when this program '
                         'ends running!\n', colors.reset)

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
    location = path + name + '.mp4'
    renametomp3 = path + name + '.mp3'
    restart.restart()


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
        print(colors.green, user_celsius, "in Celsius equals", c_to_f, "in Fahrenheit.", colors.reset)
        print(colors.green, user_celsius, "in Celsius equals", c_to_k, "in Kelvin.\n", colors.reset)
        restart.restart()
    elif user_choice == 2:
        user_fahrenheit = float(input("Fahrenheit: "))
        print()
        f_to_c = float((user_fahrenheit - 32) * 5 / 9)
        f_to_k = float((user_fahrenheit - 32) * 5 / 9 + 273.15)
        print(colors.green, user_fahrenheit, "in Fahrenheit equals", f_to_c, "in Celsius.", colors.reset)
        print(colors.green, user_fahrenheit, "in Fahrenheit equals", f_to_k, "in Kelvin.\n", colors.reset)
        restart.restart()
    elif user_choice == 3:
        user_kelvin = float(input("Kelvin: "))
        print()
        k_to_c = float(user_kelvin - 273.15)
        k_to_f = float((user_kelvin - 273.15) * 1.8 + 32)
        print(colors.green, user_kelvin, "in Kelvin equals", k_to_c, "in Celsius.", colors.reset)
        print(colors.green, user_kelvin, "in Kelvin equals", k_to_f, "in Fahrenheit.\n", colors.reset)
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
        print(colors.green, user_kilo, "in Kilograms equals", kg_to_g, "in Grams.", colors.reset)
        print(colors.green, user_kilo, "in Kilograms equals", kg_to_p, "in Pounds.", colors.reset)
        print(colors.green, user_kilo, "in Kilograms equals", kg_to_o, "in Ounces.\n", colors.reset)
        restart.restart()

    elif user_choice == 2:
        user_gram = float(input("Grams: "))
        print()
        g_to_kg = float(user_gram / 1000)
        g_to_p = float(user_gram / 454)
        g_to_o = float(user_gram / 28.35)
        print(colors.green, user_gram, "in Grams equals", g_to_kg, "in Kilograms.", colors.reset)
        print(colors.green, user_gram, "in Grams equals", g_to_p, "in Pounds.", colors.reset)
        print(colors.green, user_gram, "in Grams equals", g_to_o, "in Ounces.\n", colors.reset)
        restart.restart()

    elif user_choice == 3:
        user_pound = float(input("Pounds: "))
        print()
        p_to_kg = float(user_pound / 2.205)
        p_to_g = float(user_pound * 454)
        p_to_o = float(user_pound * 16)
        print(colors.green, user_pound, "in Pounds equals", p_to_kg, "in Kilograms.", colors.reset)
        print(colors.green, user_pound, "in Pounds equals", p_to_g, "in Grams.", colors.reset)
        print(colors.green, user_pound, "in Pounds equals", p_to_o, "in Ounces.\n", colors.reset)
        restart.restart()

    elif user_choice == 4:
        user_ounce = float(input("Ounces: "))
        print()
        o_to_kg = float(user_ounce / 35.274)
        o_to_g = float(user_ounce * 28.35)
        o_to_p = float(user_ounce / 16)
        print(colors.green, user_ounce, "in Ounces equals", o_to_kg, "in Kilograms.", colors.reset)
        print(colors.green, user_ounce, "in Ounces equals", o_to_g, "in Grams.", colors.reset)
        print(colors.green, user_ounce, "in Ounces equals", o_to_p, "in Pounds.\n", colors.reset)
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        mass_converter()


def start():
    choice = int(input('''
(1) Temperature Converter
(2) Mass Converter
(3) Currency Converter
(4) YouTube to MP3 Converter
(5) Restart
(6) Quit
What converter would you like to perform: '''))
    print()

    if choice == 1:
        temp_converter()
    elif choice == 2:
        mass_converter()
    elif choice == 3:
        currency_converter()
    elif choice == 4:
        youtube_converter()
    elif choice == 5:
        restart.restart()
    elif choice == 6:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        start()

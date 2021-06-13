import time
import colors
import restart

scale = str


def start():
    global scale
    print(colors.yellow + '''
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. 
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater.\n''', colors.reset)
    cm = int(input("Height (Centimeters): "))
    print()
    kg = int(input("Weight (Kilograms): "))
    print()

    if cm <= 0 or kg <= 0:
        print(colors.red + 'An User Input Error has been found...\n', colors.reset)
        time.sleep(2)
        start()

    else:
        formula = kg / (cm * cm) * 10000

        if formula <= 18.5:
            scale = 'Underweight'
        elif 18.6 <= formula <= 24.9:
            scale = 'Normal Weight'
        elif 25 <= formula <= 29.9:
            scale = 'Overweight'
        elif formula >= 30:
            scale = 'Obese'

        print(colors.green, 'Your BMI Measurement is:', formula, scale, colors.reset, '\n')
        time.sleep(1)
        restart.restart()


if __name__ == '__main__':
    start()

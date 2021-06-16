import time
import colors
import restart
from tools import repeat_input


def start():
    print(colors.yellow + '''
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. 
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater.\n''', colors.reset)
    cm = int(repeat_input("Height (Centimeters): ", "Invalid Height...\n", "float"))
    print()
    kg = int(repeat_input("Weight (Kilograms): ", "Invalid Weight...\n", "float"))
    print()

    if cm <= 0:
        print(colors.red + 'Error: Height Must Be More Than 0', colors.reset)
        time.sleep(2)
        start()

    elif kg <= 0:
        print(colors.red + 'Error: Weight Must Be More Than 0', colors.reset)
        time.sleep(2)
        start()

    formula = kg / (cm * cm) * 10000
    scale = str

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

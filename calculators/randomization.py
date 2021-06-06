import random
import time
import colors
import restart


def random_number():
    start_number = int(input('Pick a starting number: '))
    end_number = int(input('Pick a ending number: '))
    print()
    number = random.randint(start_number, end_number)
    print(colors.green, 'Your random generated number:',
          number, '\n', colors.reset)
    restart.restart()


def heads_or_tails():
    choice = str(input('Pick heads or tails: '))
    print()

    if choice.lower() not in ['heads', 'h', 't', 'tails', 'tail', 'head']:
        print(colors.red, 'User input error found! Restarting heads or tails...')
        time.sleep(2)
        heads_or_tails()

    else:
        coin_flip = ['heads', 'tails']
        print('You have picked:', choice)
        print('The coin flip landed on:', random.choice(coin_flip), '\n')
        restart.restart()


def start():
    choice = int(input("""(1) Random Number Generator
(2) Heads or Tails 
Which calculation would you like to perform: """))
    print()

    if choice == 1:
        random_number()
    elif choice == 2:
        heads_or_tails()
    else:
        print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)
        time.sleep(1)
        start()

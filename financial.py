# Financial code still in progress

import time
import restart
import colors

def payroll():
    print("in progress...")

def salary():
    choice = float(input("How much money do you make weekly: "))
    print()
    
    if choice <= 0:
        print(colors.red+"Please select a valid positive salary, having a salary below or equal to 0 is not possible.",colors.reset)
        time.sleep(2)
        salary()
    
    else:
        bi_weekly = choice * 2
        monthly = choice * 4
        semi_annual = monthly * 6
        annual = monthly * 12
        decade = annual * 10
        print("in progress...")
        
    
def tipping():
    choice = float(input("How much is your total bill: "))
    print()
    people_number = int(input("How many people: "))
    
    if choice <= 0:
        print(colors.red+"Please select a valid positive bill amount, having a bill amount below or equal to 0 is not possible.",colors.reset)
        time.sleep(2)
        tipping()
    
    elif people_number <= 0:
        print(colors.red+"Please select a valid positive amount of people, having an amount of people below or equal to 0 is not possible.",colors.reset)
        time.sleep(2)
        tipping()
    
    else:
        five_percent = choice * 0.5 / people_number
        ten_percent = choice * 0.10 / people_number
        fifthteen_percent = choice * 0.15 / people_number
        twenty_percent = choice * 0.20 / people_number
        twentyfive_percent = choice * 0.25 / people_number
        print("in progress")
    
    

def start():
    choice = int(input("""(1) Payroll Calculator
(2) Salary Calculator
(3) Restaurant Tip Calculator
Which calculation would you like to perform: """))
    print()
    
    if choice == 1:
        payroll()
    elif choice == 2:
        salary()
    elif choice == 3:
        tipping()
    else:
        print(colors.red+"User input error found... Restarting user input choice...\n",colors.reset)
        time.sleep(1)
        start()

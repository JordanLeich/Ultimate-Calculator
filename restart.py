# Made by Jordan Leich on 6/16/2020


# restart of program function
def restart():
    import time
    import end
    import colors

    user_restart_choice = str(input("Do you wish to restart (yes / no): "))
    print()
    time.sleep(1)

    if user_restart_choice.lower() == 'y' or user_restart_choice.lower() == 'yes':
        print("Restarting program...\n")
        time.sleep(1.5)
        import main
        main.start()

    elif user_restart_choice.lower() == 'n' or user_restart_choice.lower() == 'no':
        end.end()

    else:
        print(colors.red+"Invalid input... Restarting input...\n"+colors.reset)
        time.sleep(2)
        restart()


if __name__ == '__main__':
    restart()

import random

answer = 'y'

print('Welcome to the Fortune Teller!')
print('You will select a color and a number and I will tell you what the future holds for you!')

while answer == 'y':

    color = input("Select a color [yellow, green, blue, red]: ")

    if color == "yellow" or color == "green":
        number = int(input("Select a number [1, 2, 5, 6]: "))

        if number == 1:
            print("Worried about your future career? Don't worry. You'll 100% get what you want, be patient!")
        elif number == 2:
            print("You will become a millionaire at the age of 35!")
        elif number == 5:
            print("You will have a great family with 10 kids!")
        else:
            print("Numbers 1, 2, 5, 6 are the only numbers allowed")
    elif color == "blue" or color == "red":
        number = int(input("Select a number [3, 4, 7, 8]: "))
        if number == 3:
            print("You will live a happy life for 100 years at least!")
        elif number == 4:
            print("You will become a successful doctor one day")
        elif number == 7:
            print("All your dreams will come true, just be patient!")
        elif number == 8:
            print("You're lucky, you will have it all one day!")
        else:
            print("Numbers 3, 4, 7, 8 are the only numbers allowed")
    else:
        print("Colors [yellow, green, blue, red] aare only allowed.")

    answer = input("Play again? Insert 'y' for YES or 'n' for NO: ")

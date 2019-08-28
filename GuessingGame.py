import random

true_number = random.randint(1, 49)
print("The true number is {}".format(true_number))

guess_number = int(input("Enter a number between 1 and 49: "))

while True:
    if guess_number == true_number:
        print("YOU ARE RIGHT! GOOD JOB!")
        break
    elif guess_number < true_number:
        print("YOUR GUESS IS LOW, TRY AGAIN")
        guess_number = int(input("Enter a number between {} and 49: ".format(guess_number)))
    else:
        print("YOUR GUESS IS HIGH, TRY AGAIN")
        guess_number = int(input("Enter a number between 1 and {}: ".format(guess_number)))

import random

top_of_range= input("Type any Number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("Please Enter a Number next time!")
    quit()

random_number = random.randint(0,top_of_range)

guesses= 0

while True: # While Loop!!

    guessed_number= input("Enter Your Guess:")
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
    else:
        print("Please Enter a Number!")  
        continue

    if random_number==guessed_number:
        print("Congratulations!! You Win!")
        break # End a While Loop!!
    elif random_number > guessed_number:
        print("HINT: The number you guessed is a bit lower than the Answer ;) ")
    elif random_number < guessed_number:
        print("HINT: The number you guessed is a bit higher than the Answer ;) ")
    guesses+=1

print("Total No. of Guesses:",guesses+1)

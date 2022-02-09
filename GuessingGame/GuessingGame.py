import random 
number = random.randint(1,9)

chances = 5

while chances > 0 :
    guess = int(input("Enter a number between 0-9 : "))

    if guess == number :
        print("Congratulations! You won")
        break

    elif guess < number :
        print("Your number was too low")

    else  :
        print("Your number is too high")

    chances -= 1

    if chances == 0 :
        print("You lose, the number was",number)
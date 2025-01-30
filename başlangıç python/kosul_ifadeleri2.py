import random

right=random.randint(1,10)

print("Guess a number between 1-10: ")
guess=input()

if guess==right:
    print("Congrats! You guessed right.")
else:
    print(f"Sorry, wrong guess. The correct number was {right}.")
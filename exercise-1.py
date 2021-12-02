#!/usr/bin/env python3.10
import random

def guessing_game():
    correct_guess = random.randint(0, 100)
    print("Let's play!\nYou have three chances to guess what number has been chosen from 0 to 100.")
    
    chances = 3
    while True:

        try:
            user_answer = int(input('Please, enter your guess: '))
        except ValueError:
            print('Please, enter a valid integer number.\n')
            continue
            
        if user_answer == correct_guess:
            print(f'Right! The answer is {user_answer}.')
            break
        elif user_answer > correct_guess:
            print('Too high!')
            chances = chances - 1
        else:
            print('Too low!')
            chances = chances - 1

        if chances == 0:
            print("No more chances!")
            break

if __name__== "__main__":
    guessing_game()
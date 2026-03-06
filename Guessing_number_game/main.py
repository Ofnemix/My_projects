import random

numbers_list = list(range(0, 100 + 1))
computer_number_choice = random.choice(numbers_list)

correct_number = computer_number_choice

user_attempts = 0
easy_turn = 10
hard_turns = 5
user_answer = 0
game_over = False


def game():
    global easy_turn, hard_turns, user_attempts, game_over, user_answer

    print("Welcome to the Number Guessing Game!")
    difficulty_choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_choose == 'easy':
        user_attempts = easy_turn
        print(f"I am thinking of a number from 1 to 100... You have {user_attempts} attempts to guess the number!")
        while not game_over:
            user_answer = int(input("Insert the correct number: "))
            if user_answer != correct_number:
                user_attempts -= 1
                if user_answer < correct_number and user_attempts > 0:
                    print(f"Wrong! Too low.")
                    print(f"Try again! Attempts lefts are: {user_attempts}.")
                elif user_answer > correct_number and user_attempts > 0:
                    print("Wrong! Too High")
                    print(f"Try again! Attempts left are: {user_attempts}.")
                elif user_attempts == 0:
                    game_over = True
                    print(f"You lose! The correct number was: {correct_number}.")
            elif user_answer == correct_number:
                print(f"You won! The correct number was: {correct_number}.")
                game_over = True

    if difficulty_choose == 'hard':
        user_attempts = hard_turns
        print(f"I am thinking of a number from 1 to 100... You have {user_attempts} attempts to guess the number!")
        while not game_over:
            user_answer = int(input("Insert the correct number: "))
            if user_answer != correct_number:
                user_attempts -= 1
                if user_answer < correct_number and user_attempts > 0:
                    print(f"Wrong! Too low.")
                    print(f"Try again! Attempts left: {user_attempts}.")
                elif user_answer > correct_number and user_attempts > 0:
                    print("Wrong! Too High")
                    print(f"Try again! Attempts left: {user_attempts}.")
                elif user_attempts == 0:
                    game_over = True
                    print(f"You lose! The correct number was: {correct_number}.")
            elif user_answer == correct_number:
                print(f"You won! The correct number was: {correct_number}.")
                game_over = True

game()



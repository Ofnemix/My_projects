import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';',
           '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

def start():
    print("Hello! Welcome to the Password Generator!")
    n_letters = int(input("How many letters?: "))
    n_numbers = int(input("How many numbers?: "))
    n_symbols = int(input("How many symbols?: "))
    password = []
    for _ in range(n_letters):
        user_letters = random.choice(letters)
        password += user_letters
    for _ in range(n_numbers):
        user_numbers = random.choice(numbers)
        password += user_numbers
    for _ in range(n_symbols):
        user_symbols = random.choice(symbols)
        password += user_symbols

    random.shuffle(password)
    print(f"Your password is: {"".join(password)}")

start()
while input("Do you want to restart? Type 'y' to restart or 'n' to stop: ") == "y":
    start()
    if "n":
        print("Bye!")
        break





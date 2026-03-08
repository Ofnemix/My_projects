

check_list = []
bill = 0
menu = {
    "First Option": "Margherita Pizza",
    "Second Option": "Burger",
    "Third Option":"Salad",
    "Fourth Option":"Fries",
    "Fifth Option":"Cola",
    "Sixth Option":"Water",
    }

price_list = {
    "Margherita Pizza": 8.50,
    "Burger": 7.00,
    "Salad": 5.50,
    "Fries": 3.00,
    "Cola": 2.00,
    "Water": 1.00,

    }


print(f"Hello! Welcome to the delivery app!")

def menu_list():
    print(f"\nHere is the Menu: "
    f"\n {menu["First Option"]}: ${price_list["Margherita Pizza"]},"
    f"\n {menu["Second Option"]}: ${price_list["Burger"]},"
    f"\n {menu["Third Option"]}: ${price_list["Salad"]},"
    f"\n {menu["Fourth Option"]}: ${price_list["Fries"]},"
    f"\n {menu["Fifth Option"]}: ${price_list["Cola"]},"
    f"\n {menu["Sixth Option"]}: ${price_list["Water"]}.")


menu_list()
user_choice = input("What would you like to order? ").lower()
def order():
    global user_choice, check_list, bill
    if user_choice == "Margherita Pizza".lower() or user_choice == "Pizza".lower():
        check_list.append(user_choice)
        bill +=  price_list["Margherita Pizza"]

    elif user_choice == "Burger".lower():
        check_list.append(user_choice)
        bill += price_list["Burger"]

    elif user_choice == "Salad".lower():
        check_list.append(user_choice)
        bill += price_list["Salad"]

    elif user_choice == "Fries".lower():
        check_list.append(user_choice)
        bill += price_list["Fries"]

    elif user_choice == "Cola".lower():
        check_list.append(user_choice)
        bill += price_list["Cola"]

    elif user_choice == "Water".lower():
        check_list.append(user_choice)
        bill += price_list["Water"]
    else:
        print("Sorry! That's not on the menu. Please try again!")
        user_choice = input("What would you like to order? ").lower()
        order()
order()

another_order = input("Would you like to add anything else to your order? (y/n) ").lower()
if another_order == "y":
    while another_order == "y":
        user_choice = input("What would you like to order? ").lower()
        order()
        another_order = input("Would you like to add anything else to your order? (y/n) ").lower()
    else:
        print(f"Your order is: {", ".join(check_list)}.")
        print(f"Your total bill is: ${bill}")
else:
    print(f"Your order is: {", ".join(check_list)}.")
    print(f"Your total bill is: ${bill}")

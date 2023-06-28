prices = {"top": 50, "trousers": 75, "dress": 150}
balance = 100


class ThreeFailedAttempts(Exception):
    pass

def purchase(item, balance):
    if balance >= prices.get(item):
        return True
    else:
        return False

def goodbye(item):
    print(f"Here’s your {item}!\n")
    print("Thanks for coming to the shop. Come again!")
    exit(0)

def retry_purchase(item, balance, attempts=1):
    if attempts == 3:
        raise ThreeFailedAttempts("Your payment has failed 3 times. Please exit the store.")
    more_money = input("Your payment has failed, do you have any more money? (Y/N)")
    if more_money == "Y":
        try:
            balance += float(input("How much?"))
        except ValueError:
            raise ValueError("Invalid input, exiting store")
    if purchase(item, balance):
        goodbye(item)
    else:
        attempts += 1
        retry_purchase(item, balance, attempts)

def welcome():
    print("Welcome to the clothes shop!")
    print("We have the following items available:")
    for item in prices:
        print(f"{item} - £{prices.get(item)}")

    choice = input("\nWhat would you like to buy?\nEnter 'exit' to exit the shop\n")

    if choice == "exit":
        exit(0)
    elif choice in prices.keys():
        if purchase(choice, balance):
            goodbye(choice)
        else:
            retry_purchase(choice, balance)
    else:
        raise ValueError("Not a valid answer, please return and try again")
# Day 15 - Intermediate - Installing pycharm

# Day 15 - Project - Coffee Machine
from Day15_data import commands, MENU, resources

def check_resources(menu_item, current_resources):
    not_available_resources = []
    for i in menu_item["ingredients"]:
        if menu_item["ingredients"][i] > current_resources[i]:
            not_available_resources.append(f"Sorry! There is not enough {i}")
    return not_available_resources

def alter_resources(menu_item, current_resources):
    for i in menu_item["ingredients"]:
        current_resources[i] -= menu_item["ingredients"][i]
    return current_resources    

def get_change(item_cost, quarters, dimes, nickels, pennies):
    # do the operation normall, and check on call to see if the return value is negative
    return quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01 - item_cost
def print_commands():
    print("Here's a list of other general commands you can use. Enjoy!")
    for i in commands:
        print(f"{i} - {commands[i]}")
  
def coffee_machine():
    transaction_list = []
    current_resources = resources.copy()
    money = 0
    total_cash = 0
    while True:
        choice = input("What would you like? espresso/latte/cappuccino (h for help): ").lower()
        if choice in ["h","help"]:
            print_commands()
        elif choice == "transactions":
            if len(transaction_list) == 0:
                print("No transactions yet.")
                continue
            print("Here's a list of all the transactions: ")
            for i in range(len(transaction_list)):
                print("-"*60)
                print(f"||Order #{i+1}: Item: {transaction_list[i]['item']} -- Cost: {MENU[transaction_list[i]['item']]['cost']} -- Change: {transaction_list[i]['change']}||")
                print("-"*60)
        elif choice == "off":
            return
        elif choice == "menu":
            for i in MENU:
                print(f"Buy {i} for: ${MENU[i]['cost']}")
        elif choice == "refill":
            current_resources = resources.copy()
            print("All ingredients refilled. Keep Going!")
        elif choice == "cashout":
            money = 0
            print("All cashed out!")
        elif choice == "totalpurchase":
            print(f"This machine has earnt ${round(total_cash*0.25, 2)} (excl. taxes)")
        elif choice == "report":
            print(f"Water: {current_resources['water']}ml\nMilk: {current_resources['milk']}ml\nWater: {current_resources['coffee']}g\nMoney: ${money}")
        elif choice in MENU:
            menu_item = MENU[choice]
            # check if machine has enough resources to fulfill the request
            not_available_resources = check_resources(menu_item, current_resources)
            if len(not_available_resources) != 0:
                for resource_message in not_available_resources:
                    print(resource_message)
            else:
                # There are enough resources, check if the guy has enough money
                item_cost = menu_item["cost"]
                print("Please insert coin(s), just press `Enter` if you dont want to put in the coin")
                quarters = input("How many quarters?: ")
                dimes = input("How many dimes?: ")
                nickels = input("How many nickels?: ")
                pennies = input("How many pennies?: ")
                quarters = int(quarters) if quarters != '' else 0
                dimes = int(quarters) if dimes != '' else 0
                nickels = int(quarters) if nickels != '' else 0
                pennies = int(quarters) if pennies != '' else 0
                change = round(get_change(item_cost, quarters, dimes, nickels, pennies),2)
                
                if change < 0:
                    print("Sorry that's not enough money. Money refunded.")
                    
                else:
                    current_resources = alter_resources(menu_item, current_resources)
                    money += item_cost
                    total_cash += money
                    transaction_list.append({"item": choice, "change": change})
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice} ☕️. Enjoy!")
            

coffee_machine()
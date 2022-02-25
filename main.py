from data import MENU, resources

# start the machine
is_on = True
profit = 0
options = ['latte', 'cappuccino', 'espresso', 'report', 'off']


def report():
    for i in resources:
        print(f'{i} : {resources[i]}')
    print(f'Total Profit : {profit}')


def check_resource(ing):
    for i in ing:
        if ing[i] >= resources[i]:
            print(f'Sorry not enough {i}')
            return False
    return True


def coins_process():
    """Takes coins from user and returns sum of coins"""
    print('Please insert coins')
    total = int(input('How many quarters:  '))*0.25         # calculate the coin  will accepting the data
    total += int(input('How many Nickels : '))*0.05
    total += int(input('How many dimes : ')) * 0.1
    total += int(input('How many pennies : ')) * 0.01
    return total


def check_money(payment, drink_cost):
    """Return True if payment is sufficent else returns False on failure"""

    if payment < drink_cost:
        print('Sorry you do not  have enough money')
        return False

    global profit
    profit += drink_cost
    change = round(payment - drink_cost, 2)
    print(f'Here is your change  : ${change}')
    return True


def make_coffee(drink, ing):
    for item in ing:
        resources[item] -= ing[item]
    print(f'Here is your coffee : {drink}')


while is_on:
    choice = input('What would you want  : (latte ,  cappuino , expresso) ').lower()
    if choice not in options:
        print('Invalid choice !')
        break

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report()
    else:
        order = MENU[choice]
        ingredients = MENU[choice]['ingredients']
        if check_resource(ingredients):
            payment = coins_process()
            if check_money(payment, order['cost']):
                make_coffee(choice, order['ingredients'])

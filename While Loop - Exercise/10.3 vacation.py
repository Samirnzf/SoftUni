money_needed = float(input())
balance = float(input())
days_counter = 0
spending_counter = 0
spending_in_a_row = False
while balance < money_needed:
    action = input()
    money = float(input())
    days_counter += 1
    if action == "spend":
        spending_counter += 1
        if spending_counter == 5:
            spending_in_a_row = True
            break
        balance -= money
        if balance < 0:
            balance = 0
    elif action == "save":
        balance += money
        spending_counter = 0
if spending_in_a_row:
    print("You can't save the money.")
    print(days_counter)

else:
    print(f"You saved the money for {days_counter} days.")

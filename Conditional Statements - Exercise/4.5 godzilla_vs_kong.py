film_budget = float(input())
number_of_statists = int(input())
clothing_for_each = float(input())
clothing_price = number_of_statists * clothing_for_each
decor = film_budget * 0.10

if number_of_statists > 150:
    clothing_price *= 0.90

total_expense = clothing_price + decor
difference = abs(film_budget - total_expense)

if total_expense > film_budget:
    print("Not enough money!")
    print(f'Wingard needs {difference:.2f} leva more.')
elif total_expense <= film_budget:
    print("Action!")
    print(f'Wingard starts filming with {difference:.2f} leva left.')







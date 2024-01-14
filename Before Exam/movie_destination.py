budget = float(input())
destination = input()
season = input()
days = int(input())
price_for_one_day = 0
total_cost = 0

if destination == 'Dubai':
    total_cost *= 0.70
    if season == 'Summer':
        price_for_one_day += 40000
    elif season == 'Winter':
        price_for_one_day += 45000

if destination == 'Sofia':
    total_cost *= 1.25
    if season == 'Summer':
        price_for_one_day += 12500
    elif season == 'Winter':
        price_for_one_day += 17000

if destination == 'London':
    if season == 'Summer':
        price_for_one_day += 20250
    elif season == 'Winter':
        price_for_one_day += 24000

if destination == 'Dubai':
    total_cost *= 0.70


total_cost = price_for_one_day * days

if destination == 'Dubai':
    total_cost *= 0.70

elif destination == 'Sofia':
    total_cost *= 1.25

difference = f'{abs(total_cost - budget):.2f}'

if budget >= total_cost:
    print(f'The budget for the movie is enough! We have {difference} leva left!')
else:
    print(f'The director needs {difference} leva more!')

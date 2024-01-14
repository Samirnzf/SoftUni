budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percentage_for_other_costs = int(input())

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

price_for_vacation = number_of_nights * price_per_night
additional_costs = budget * (percentage_for_other_costs / 100)
total_cost = price_for_vacation + additional_costs

difference = f'{abs(total_cost - budget):.2f}'

if total_cost <= budget:
    print(f'Ivanovi will be left with {difference} leva after vacation.')
else:
    print(f'{difference} leva needed.')

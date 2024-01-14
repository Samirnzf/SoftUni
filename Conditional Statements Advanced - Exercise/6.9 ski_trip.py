days = int(input())
type_of_room = input()
value = input()
nights = days - 1
price_per_night = 0
if type_of_room == "room for one person":
    price_per_night = 18.00
elif type_of_room == "apartment":
    price_per_night = 25.00
    if nights < 10:
        price_per_night *= 0.70
    elif nights <= 15:
        price_per_night *= 0.65
    elif nights > 15: # else
        price_per_night *= 0.50
elif type_of_room == "president apartment":
    price_per_night = 35.00
    if nights < 10:
        price_per_night *= 0.90
    elif nights <= 15:
        price_per_night *= 0.85
    elif nights > 15: # else
        price_per_night *= 0.80

total_sum = price_per_night * nights

if value == "positive":
    total_sum *= 1.25
elif value == "negative":
    total_sum *= 0.90

print(f'{total_sum:.2f}')


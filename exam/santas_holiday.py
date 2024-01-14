days_of_vacation = int(input())
type_of_room = input()
feedback = input()
nights = days_of_vacation - 1
price_for_room_1 = 18.00
price_for_apartment = 25.00
price_for_president_apartment = 35.00
price_for_vacation = 0
if type_of_room == 'room for one person':
    price_for_vacation += price_for_room_1 * nights

if type_of_room == 'apartment':
    price_for_vacation += price_for_apartment * nights
    if nights < 10:
        price_for_vacation *= 0.70
    elif 10 <= nights <= 15:
        price_for_vacation *= 0.65
    elif nights > 15:
        price_for_vacation *= 0.50

elif type_of_room == 'president apartment':
    price_for_vacation += price_for_president_apartment * nights
    if nights < 10:
        price_for_vacation *= 0.90
    elif 10 <= nights <= 15:
        price_for_vacation *= 0.85
    elif nights > 15:
        price_for_vacation *= 0.80

if feedback == 'positive':
    price_for_vacation *= 1.25
elif feedback == 'negative':
    price_for_vacation *= 0.90

print(f'{price_for_vacation:.2f}')



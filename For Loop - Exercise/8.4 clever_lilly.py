age = int(input())
laundry_price = float(input())
price_for_one_toy = int(input())
gift_money = 0
amount_of_toys = 0
saved_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        gift_money += 10
        saved_money += gift_money - 1
    elif birthday % 2 != 0:
        amount_of_toys += 1

saved_money += price_for_one_toy * amount_of_toys
difference = abs(saved_money - laundry_price)

if saved_money >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")

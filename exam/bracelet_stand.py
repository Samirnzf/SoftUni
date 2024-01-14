pocket_money = float(input())
sales = float(input())
expenses = float(input())
gift_price = float(input())

saved_pocket_money = pocket_money * 5
profit_money = sales * 5
saved_money = saved_pocket_money + profit_money - expenses

if saved_money >= gift_price:
    print(f'Profit: {saved_money:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {gift_price - saved_money:.2f} BGN.')




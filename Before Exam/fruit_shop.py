strawberry_price = float(input())
bananas_qty = float(input())
oranges_qty = float(input())
berry_qty = float(input())
strawberry_qty = float(input())

berry_price = strawberry_price / 2
oranges_price = berry_price * 0.60
bananas_price = berry_price * 0.20

price_of_all_bananas = bananas_price * bananas_qty
price_of_all_oranges = oranges_price * oranges_qty
price_of_all_berries = berry_price * berry_qty
price_of_all_strawberries = strawberry_price * strawberry_qty

total_sum = price_of_all_bananas + price_of_all_oranges \
            + price_of_all_berries + price_of_all_strawberries

print(f'{total_sum:.2f}')

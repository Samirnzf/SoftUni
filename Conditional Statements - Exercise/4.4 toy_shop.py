vacation_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_plush_minions = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle = 2.60
doll = 3.00
plush_minion = 4.10
minion = 8.20
truck = 2.00

toys_amount = number_of_trucks + number_of_minions \
    + number_of_plush_minions + number_of_dolls \
    + number_of_puzzles

toys_price = puzzle * number_of_puzzles \
             + doll * number_of_dolls \
             + plush_minion * number_of_plush_minions \
             + minion * number_of_minions \
             + truck * number_of_trucks


if toys_amount >= 50:
    toys_price *= 0.75

toys_price *= 0.90
difference = abs(toys_price - vacation_price)

if toys_price >= vacation_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
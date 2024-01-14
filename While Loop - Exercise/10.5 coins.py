change = float(input())
coins = 0
change = change * 100

while coins <= change:
    current_coins = int(change / 200)
    change -= current_coins * 200
    coins += current_coins

    current_coins = int(change / 100)
    change -= current_coins * 100
    coins += current_coins

    current_coins = int(change / 50)
    change -= current_coins * 50
    coins += current_coins

    current_coins = int(change / 20)
    change -= current_coins * 20
    coins += current_coins

    current_coins = int(change / 10)
    change -= current_coins * 10
    coins += current_coins

    current_coins = int(change / 5)
    change -= current_coins * 5
    coins += current_coins

    current_coins = int(change / 2)
    change -= current_coins * 2
    coins += current_coins

    current_coins = int(change)
    coins += current_coins

print(coins)
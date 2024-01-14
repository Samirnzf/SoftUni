destination = input()
budget = saved_money = 0

while destination != 'End':
    budget = float(input())
    if budget > 0:
        while budget > saved_money:
            money = float(input())
            if money > 0:
                saved_money += money
                if saved_money >= budget:
                    print(f'Going to {destination}!')
                    saved_money = 0
            if saved_money == 0:
                break
    destination = input()

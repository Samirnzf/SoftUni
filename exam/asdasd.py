number = int(input())
number_found = False
counter = 0
for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                if (a + b + c + d) == (a * b * c * d) and number % 10 == 5:
                    counter += 1
                    print(f'{a}{b}{c}{d}')
                    number_found = True
                    break
                elif (a * b * c * d) // (a + b + c + d) == 3 and number % 3 == 0:
                    counter += 1
                    print(f'{d}{c}{b}{a}')
                    number_found = True
                    break
            if number_found:
                break
        if number_found:
            break
    if number_found:
        break
if counter == 0:
    print("Nothing found")

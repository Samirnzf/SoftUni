from math import inf

min_number = inf

while True:
    text = input()

    if text == "Stop":
        print(min_number)
        break

    current_number = int(text)

    if current_number < min_number:
        min_number = current_number

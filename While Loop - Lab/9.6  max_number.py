from math import inf

max_number = -inf

while True:
    text = input()

    if text == "Stop":
        print(max_number)
        break

    current_number = int(text)

    if current_number > max_number:
        max_number = current_number

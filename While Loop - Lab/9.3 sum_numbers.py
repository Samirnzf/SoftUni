NUMBER = int(input())
number_counter = 0

while True:
    current_number = int(input())
    number_counter += current_number

    if number_counter >= NUMBER:
        print(number_counter)
        break

from math import inf

numbers = int(input())
total_sum = 0
max_element = -inf

for number in range(numbers):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_element:
        max_element = current_number
if max_element == total_sum - max_element:
    print("Yes")
    print(f'Sum = {max_element}')
else:
    difference = abs(max_element - (total_sum - max_element))
    print("No")
    print(f"Diff = {difference}")

user_input = input()
user_output = 'unknown'

if user_input == 'banana' or user_input == 'apple' \
        or user_input == 'kiwi' or user_input == 'cherry' \
        or user_input == 'lemon' or user_input == 'grapes':
    user_output = 'fruit'

elif user_input == 'tomato' or user_input == 'cucumber' \
        or user_input == 'pepper' or user_input == 'carrot':
    user_output = 'vegetable'

print(user_output)


# Read user input
user_input = int(input())
user_output = 'Error'

# Logic
if user_input == 1:
    user_output = 'Monday'
elif user_input == 2:
    user_output = 'Tuesday'
elif user_input == 3:
    user_output = 'Wednesday'
elif user_input == 4:
    user_output = 'Thursday'
elif user_input == 5:
    user_output = 'Friday'
elif user_input == 6:
    user_output = 'Saturday'
elif user_input == 7:
    user_output = 'Sunday'


# Print output
print(user_output)

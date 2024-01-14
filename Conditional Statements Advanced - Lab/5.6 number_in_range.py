# Read user input
number = int(input())
user_output = ''
# Logic
if number >= -100 and number <= 100 and number != 0: # if -100 <= num <= 100:
    user_output = 'Yes'
else:
    user_output = 'No'

# Print output
print(user_output)
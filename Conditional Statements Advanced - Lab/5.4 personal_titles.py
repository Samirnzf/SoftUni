age = float(input())
gender = input()
user_output = ''

if gender == 'm':
    user_output = 'Mr.'
    if age < 16:
        user_output = 'Master'

elif gender == 'f':
    user_output = 'Ms.'
    if age < 16:
        user_output = 'Miss'

print(user_output)

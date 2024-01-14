goal = int(input())
income = 0
while income < goal:
    command = input()
    if command != "closed":
        age_group = input()
        if command == "haircut":
            if age_group == "mens":
                income += 15
            if age_group == "ladies":
                income += 20
            if age_group == "kids":
                income += 10
        if command == "color":
            if age_group == "touch up":
                income += 20
            if age_group == "full color":
                income += 30
    if command == "closed":
        break

diff = abs(goal - income)

if income >= goal:
    print("You have reached your target for the day!")
elif income < goal:
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {income}lv.")

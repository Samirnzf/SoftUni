tabs_opened = int(input())
salary = int(input())

for websites in range(tabs_opened):
    opened_website = input()
    if opened_website == "Facebook":
        salary -= 150
    elif opened_website == "Instagram":
        salary -= 100
    elif opened_website == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")

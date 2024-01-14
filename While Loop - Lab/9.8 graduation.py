# input
student_name = input()
count_of_grades = 0
count_of_years = 0
count_of_failed_years = 0
# logic
while True:
    annual_grade = float(input())

    if annual_grade < 4:
        count_of_failed_years += 1
        if count_of_failed_years > 1:
            print(f"{student_name} has been excluded at {count_of_years + 1} grade")
            break
        continue

    count_of_years += 1
    count_of_grades += annual_grade

    if count_of_years == 12:
        average_grade = f"{count_of_grades / 12:.2f}"
        print(f'{student_name} graduated. Average grade: {average_grade}')
        break

actor_name = input()
academy_points = float(input())
number_of_judges = int(input())
total_points = academy_points
for judge in range(number_of_judges):
    name_of_judge = input()
    judge_points = float(input())
    total_points += ((len(name_of_judge) * judge_points) / 2)
    if total_points > 1250.5:
        break
diff = abs(total_points - 1250.5)

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")



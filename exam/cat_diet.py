percentage_fats = int(input())
percentage_protein = int(input())
percentage_carbs = int(input())
total_kcal = int(input())
percentage_water = int(input())

grams_fats = ((percentage_fats / 100) * total_kcal) / 9
grams_protein = ((percentage_protein / 100) * total_kcal) / 4
grams_carbs = ((percentage_carbs / 100) * total_kcal) / 4

total_weight = grams_fats + grams_carbs + grams_protein
weight_per_gram = total_kcal / total_weight
calories = weight_per_gram * (1 - percentage_water / 100)
print(f'{calories:.4f}')
days = int(input())
total_liters_of_rakija = 0
total_degrees_of_rakija = 0

for day in range(days):
    liters_of_rakija = float(input())
    total_liters_of_rakija += liters_of_rakija
    degree_of_rakija = float(input())
    degrees_of_rakija_for_today = liters_of_rakija * degree_of_rakija
    total_degrees_of_rakija += degrees_of_rakija_for_today

average_degrees = total_degrees_of_rakija / total_liters_of_rakija

print(f"Liter: {total_liters_of_rakija:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
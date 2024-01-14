width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
total_free_space = width_free_space * length_free_space * height_free_space
carton_size = 1 * 1 * 1
carton_count = 0
carton_space = 0

while total_free_space > carton_space:
    command = input()
    if command == "Done":
        break
    carton_count += int(command)
    carton_space = carton_size * carton_count
difference = abs(total_free_space - carton_space)
if carton_space > total_free_space:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")



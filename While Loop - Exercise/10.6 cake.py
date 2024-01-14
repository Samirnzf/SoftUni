cake_width = int(input())
cake_length = int(input())
cake = cake_length * cake_width

pieces_count = 0

while cake > pieces_count:
    command = input()

    if command == "STOP":
        break

    add = int(command)
    pieces_count += add

pieces_display = abs(cake - pieces_count)

if cake > pieces_count:
    print(f"{pieces_display} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_display} pieces more.")

record_in_seconds = float(input())
meters_to_swim = float(input())
time_for_one_meter = float(input())
time = meters_to_swim * time_for_one_meter
slowing = (meters_to_swim//15)*12.5
total_time = time + slowing

time_difference = abs(total_time - record_in_seconds)

if total_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {time_difference:.2f} seconds slower.')


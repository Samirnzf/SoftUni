import math

movie_name = input()
time_for_episode = int(input())
break_time = int(input())
lunch_time = break_time / 8
rest_time = break_time / 4
time_left = break_time - lunch_time - rest_time
free_time = abs(time_left - time_for_episode)
free_time = math.ceil(free_time)

if time_left >= time_for_episode:
    print(f'You have enough time to watch {movie_name} and left with {free_time} minutes free time.')
else:
    print(f"You don't have enough time to watch {movie_name}, you need {free_time} more minutes.")

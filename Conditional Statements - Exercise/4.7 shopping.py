budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

all_video_cards_price = number_of_video_cards * 250
one_processor_price = all_video_cards_price * 0.35
all_processors_price = number_of_processors * one_processor_price
one_ram_price = all_video_cards_price * 0.10
all_ram_price = number_of_ram * one_ram_price

total_sum = (all_video_cards_price
             + all_processors_price
             + all_ram_price)

if number_of_video_cards > number_of_processors:
    total_sum *= 0.85

difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f'You have {difference:.2f} leva left!')
elif total_sum >= budget:
    print(f'Not enough money! You need {difference:.2f} leva more!')
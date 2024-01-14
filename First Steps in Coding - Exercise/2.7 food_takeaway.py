chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())  # sum * 0.2 = desert
price_of_chicken_menu = 10.35
price_of_fish_menu = 12.40
price_of_vegan_menu = 8.15
price_of_menus = chicken_menu * price_of_chicken_menu \
    +fish_menu * price_of_fish_menu \
    +vegan_menu * price_of_vegan_menu
dessert = price_of_menus * 0.2
total_sum = price_of_menus + dessert + 2.50
print(total_sum)
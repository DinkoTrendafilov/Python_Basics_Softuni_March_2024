count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

chicken_menu_single_price = 10.35
fish_menu_single_price = 12.40
vegan_menu_single_price = 8.15
delivery_price = 2.5

sum_of_things = count_chicken_menu * chicken_menu_single_price + count_fish_menu * fish_menu_single_price \
                + vegan_menu_single_price * count_vegan_menu

desert = sum_of_things * 0.2

total_sum = sum_of_things + desert + delivery_price

print(f"{total_sum:.2f}")

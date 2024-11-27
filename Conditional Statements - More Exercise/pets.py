import math

number_of_days = int(input())
food_in_kg = int(input())
food_for_dog_kilograms = float(input())
food_for_cat_kilograms = float(input())
food_for_turtle_grams = float(input())
food_for_turtle_kilograms = food_for_turtle_grams / 1000

needed_food = number_of_days * (food_for_dog_kilograms +
                                food_for_cat_kilograms +
                                food_for_turtle_kilograms)

diff = abs(needed_food - food_in_kg)

if food_in_kg >= needed_food:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')

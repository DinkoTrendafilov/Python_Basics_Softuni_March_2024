quantity_food_for_dogs = int(input())
quantity_food_for_cats = int(input())

single_price_for_dogs = 2.5
single_price_for_cats = 4

total_costs = (quantity_food_for_dogs * single_price_for_dogs ) + (quantity_food_for_cats * single_price_for_cats)



print(f"{total_costs:.1f} lv.")
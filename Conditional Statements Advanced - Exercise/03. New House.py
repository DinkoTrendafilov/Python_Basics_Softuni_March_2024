type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

flower_price = 0

if type_of_flowers == 'Roses':
    flower_price = 5
    if number_of_flowers > 80:
        flower_price *= 0.9
elif type_of_flowers == 'Dahlias':
    flower_price = 3.8
    if number_of_flowers > 90:
        flower_price *= 0.85
elif type_of_flowers == 'Tulips':
    flower_price = 2.8
    if number_of_flowers > 80:
        flower_price *= 0.85
elif type_of_flowers == 'Narcissus':
    flower_price = 3
    if number_of_flowers < 120:
        flower_price *= 1.15
elif type_of_flowers == 'Gladiolus':
    flower_price = 2.5
    if number_of_flowers < 80:
        flower_price *= 1.20

total_price = flower_price * number_of_flowers
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
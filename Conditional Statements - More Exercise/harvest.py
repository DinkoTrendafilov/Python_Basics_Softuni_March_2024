import math

vineyard_area = float(input())
vineyard_per_meter = float(input())
needed_litres_wine = float(input())
number_of_worker = int(input())

wine_quantity = (vineyard_area * vineyard_per_meter * 0.4) / 2.5
diff = abs(needed_litres_wine - wine_quantity)

extra_wine = wine_quantity - needed_litres_wine
other_wine = extra_wine / number_of_worker

if wine_quantity < needed_litres_wine:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine_quantity)} liters.')
    print(f'{math.ceil(extra_wine)} liters left -> {math.ceil(other_wine)} liters per person.')

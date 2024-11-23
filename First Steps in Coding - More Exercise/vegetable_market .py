price_per_kilo_vegetables = float(input())
price_per_kilo_fruits = float(input())
quantity_vegetables = int(input())
quantity_fruits = int(input())

vegetable_price = price_per_kilo_vegetables * quantity_vegetables
fruits_price = price_per_kilo_fruits * quantity_fruits
total_price_in_leva = vegetable_price + fruits_price
total_in_euro = total_price_in_leva / 1.94

print(f'{total_in_euro:.2f}')
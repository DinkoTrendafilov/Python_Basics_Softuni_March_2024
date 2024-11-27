type_of_fuel = input()
fuel_quantity = float(input())
club_card = input()

price = 0
if type_of_fuel == 'Gasoline':
    price = 2.22
elif type_of_fuel == 'Diesel':
    price = 2.33
elif type_of_fuel == 'Gas':
    price = 0.93

if club_card == 'Yes' and type_of_fuel == 'Gasoline':
    price -= 0.18

elif club_card == 'Yes' and type_of_fuel == 'Diesel':
    price -= 0.12
elif club_card == 'Yes' and type_of_fuel == 'Gas':
    price -= 0.08

if 20 < fuel_quantity <= 25:
    price *= 0.92
elif fuel_quantity > 25:
    price *= 0.90

total_price = price * fuel_quantity
print(f"{total_price:.2f} lv.")

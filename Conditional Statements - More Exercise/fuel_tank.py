type_of_fuel = input().lower()
fuel_quantity = float(input())

if type_of_fuel in ('diesel', 'gasoline', 'gas'):
    if fuel_quantity < 25:
        print(f"Fill your tank with {type_of_fuel}!")
    elif fuel_quantity >= 25:
        print(f"You have enough {type_of_fuel}.")
else:
    print("Invalid fuel!")

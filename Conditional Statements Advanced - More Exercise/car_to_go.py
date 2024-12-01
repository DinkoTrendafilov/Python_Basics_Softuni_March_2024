budget = float(input())
season = input()

type_of_class = ''
type_of_car = ''
rent_cost = 0

if budget <= 100:
    type_of_class = 'Economy class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        rent_cost = budget * 0.35
    elif season == 'Winter':
        type_of_car = 'Jeep'
        rent_cost = budget * 0.65

elif 100 < budget <= 500:
    type_of_class = 'Compact class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        rent_cost = budget * 0.45
    elif season == 'Winter':
        type_of_car = 'Jeep'
        rent_cost = budget * 0.8
elif budget > 500:
    type_of_class = 'Luxury class'
    type_of_car = 'Jeep'
    rent_cost = budget * 0.9

print(f"{type_of_class}")
print(f"{type_of_car} - {rent_cost:.2f}")

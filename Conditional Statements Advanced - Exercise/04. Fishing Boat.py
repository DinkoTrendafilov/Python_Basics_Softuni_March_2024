budget = int(input())
season = input()
numbers_of_fisherman = int(input())

rent_price = 0

if season == 'Spring':
    rent_price = 3000
elif season in ('Summer', 'Autumn'):
    rent_price = 4200
elif season == 'Winter':
    rent_price = 2600

if numbers_of_fisherman <= 6:
    rent_price *= 0.9
elif 7 <= numbers_of_fisherman <= 11:
    rent_price *= 0.85
elif numbers_of_fisherman >= 12:
    rent_price *= 0.75

if numbers_of_fisherman % 2 == 0 and season != 'Autumn':
    rent_price *= 0.95

diff = abs(budget - rent_price)

if budget >= rent_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


month = input()
number_of_nights = int(input())

studio_price = 0
apartment_price = 0

if month in ('May', 'October'):
    studio_price = 50
    apartment_price = 65
    if number_of_nights > 14:
        studio_price *= 0.70
    elif number_of_nights > 7:
        studio_price *= 0.95
elif month in ('June', 'September'):
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price *= 0.8
elif month in ('July', 'August'):
    studio_price = 76
    apartment_price = 77

if number_of_nights > 14:
    apartment_price *= 0.9

total_price_apartment = number_of_nights * apartment_price
total_price_studio = number_of_nights * studio_price

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
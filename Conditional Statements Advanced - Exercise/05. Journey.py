budget = float(input())
season = input()

destination = ''
hotel_or_camp = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        hotel_or_camp = 'Camp'
        price = budget * 0.3
    elif season == 'winter':
        hotel_or_camp = 'Hotel'
        price = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        hotel_or_camp = 'Camp'
        price = budget * 0.4
    elif season == 'winter':
        hotel_or_camp = 'Hotel'
        price = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        hotel_or_camp = 'Hotel'
        price = budget * 0.9
    elif season == 'winter':
        hotel_or_camp = 'Hotel'
        price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{hotel_or_camp} - {price:.2f}")
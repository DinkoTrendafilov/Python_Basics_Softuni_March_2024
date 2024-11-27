number_of_km = float(input())
part_of_day = input()

min_price = 0
taxi_price = 0
bus_price = 0
train_price = 0

if number_of_km < 20:
    if part_of_day == 'day':
        taxi_price = 0.7 + (number_of_km * 0.79)
    elif part_of_day == 'night':
        taxi_price = 0.70 + (number_of_km * 0.90)
    min_price = taxi_price
elif 20 <= number_of_km < 100:
    if part_of_day == 'day':
        taxi_price = 0.7 + (number_of_km * 0.79)
        bus_price = (number_of_km * 0.09)
    elif part_of_day == 'night':
        taxi_price = 0.70 + (number_of_km * 0.90)
        bus_price = (number_of_km * 0.09)
    min_price = min(bus_price, taxi_price)

elif number_of_km >= 100:
    if part_of_day == 'day':
        taxi_price = 0.7 + (number_of_km * 0.79)
        bus_price = (number_of_km * 0.09)
        train_price = (number_of_km * 0.06)
    elif part_of_day == 'night':
        taxi_price = 0.70 + (number_of_km * 0.90)
        bus_price = (number_of_km * 0.09)
        train_price = (number_of_km * 0.06)
    min_price = min(bus_price, train_price, taxi_price)

print(f'{min_price:.2f}')

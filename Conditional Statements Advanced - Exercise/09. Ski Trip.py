days = int(input())
type_of_room = input()
estimate = input()
nights = days - 1

price_per_night = 0

if type_of_room == 'room for one person':
    price_per_night = 18
elif type_of_room == 'apartment':
    price_per_night = 25
    if nights < 10:
        price_per_night *= 0.7
    elif 10 <= nights <= 15:
        price_per_night *= 0.65
    elif nights > 15:
        price_per_night *= 0.50
elif type_of_room == 'president apartment':
    price_per_night = 35
    if nights < 10:
        price_per_night *= 0.9
    elif 10 <= nights <= 15:
        price_per_night *= 0.85
    elif nights > 15:
        price_per_night *= 0.80

total_price = price_per_night * nights

if estimate == 'positive':
    total_price *= 1.25
elif estimate == 'negative':
    total_price *= 0.9

print(f'{total_price:.2f}')
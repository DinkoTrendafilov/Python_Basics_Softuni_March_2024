season = input()
kilometers_per_month = float(input())

price_per_kilometer = 0

if season in ('Spring', 'Autumn'):
    if kilometers_per_month <= 5_000:
        price_per_kilometer = 0.75
    elif 5_000 < kilometers_per_month <= 10_000:
        price_per_kilometer = 0.95
    elif 10_000 < kilometers_per_month <= 20_000:
        price_per_kilometer = 1.45
elif season == 'Summer':
    if kilometers_per_month <= 5_000:
        price_per_kilometer = 0.9
    elif 5_000 < kilometers_per_month <= 10_000:
        price_per_kilometer = 1.1
    elif 10_000 < kilometers_per_month <= 20_000:
        price_per_kilometer = 1.45
elif season == 'Winter':
    if kilometers_per_month <= 5_000:
        price_per_kilometer = 1.05
    elif 5_000 < kilometers_per_month <= 10_000:
        price_per_kilometer = 1.25
    elif 10_000 < kilometers_per_month <= 20_000:
        price_per_kilometer = 1.45

total_costs = kilometers_per_month * price_per_kilometer * 4
total_costs *= 0.9

print(f'{total_costs:.2f}')

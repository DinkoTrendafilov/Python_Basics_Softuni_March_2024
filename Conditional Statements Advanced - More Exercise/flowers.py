count_hrisantemas = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
holiday_or_not = input()

total_count_flowers = count_hrisantemas + count_roses + count_tulips
price = 0
if season in ('Spring', 'Summer'):
    price = (count_hrisantemas * 2) + (count_roses * 4.1) + (count_tulips * 2.5)

elif season in ('Autumn', 'Winter'):
    price = (count_hrisantemas * 3.75) + (count_roses * 4.5) + (count_tulips * 4.15)

if holiday_or_not == 'Y':
    price *= 1.15

if count_tulips > 7 and season == 'Spring':
    price *= 0.95
if count_roses >= 10 and season == 'Winter':
    price *= 0.9
if total_count_flowers >= 20:
    price *= 0.8

price += 2

print(f'{price:.2f}')

season = input()
type_of_group = input()
students_count = int(input())
count_of_nights = int(input())

sport = ''
price_per_night = 0

if season == 'Winter':
    if type_of_group == 'girls':
        sport = 'Gymnastics'
        price_per_night = 9.6
    elif type_of_group == 'boys':
        sport = 'Judo'
        price_per_night = 9.6
    elif type_of_group == 'mixed':
        sport = 'Ski'
        price_per_night = 10
elif season == 'Spring':
    if type_of_group == 'girls':
        sport = 'Athletics'
        price_per_night = 7.2
    elif type_of_group == 'boys':
        sport = 'Tennis'
        price_per_night = 7.2
    elif type_of_group == 'mixed':
        sport = 'Cycling'
        price_per_night = 9.5
elif season == 'Summer':
    if type_of_group == 'girls':
        sport = 'Volleyball'
        price_per_night = 15
    elif type_of_group == 'boys':
        sport = 'Football'
        price_per_night = 15
    elif type_of_group == 'mixed':
        sport = 'Swimming'
        price_per_night = 20

total_price = price_per_night * count_of_nights * students_count

if students_count >= 50:
    total_price *= 0.5
elif 20 <= students_count < 50:
    total_price *= 0.85
elif 10 <= students_count < 20:
    total_price *= 0.95

print(f'{sport} {total_price:.2f} lv.')

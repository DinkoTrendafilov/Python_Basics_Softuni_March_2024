hour_of_day = int(input())
day_of_week = input()

if 10 <= hour_of_day <= 18 and day_of_week != 'Sunday':
    print('open')
else:
    print('closed')
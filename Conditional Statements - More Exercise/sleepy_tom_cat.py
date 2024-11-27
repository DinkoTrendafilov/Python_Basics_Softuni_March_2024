days_of_holiday = int(input())

norm_of_play_in_minutes = 30_000

work_days = 365 - days_of_holiday
work_days_playing = work_days * 63
holidays_playing = days_of_holiday * 127
total_playing = work_days_playing + holidays_playing

diff = abs(norm_of_play_in_minutes - total_playing)
hours = diff // 60
minutes = diff % 60

if norm_of_play_in_minutes > total_playing:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
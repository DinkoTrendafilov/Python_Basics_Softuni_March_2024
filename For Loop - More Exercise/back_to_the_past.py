money = float(input())
end_year = int(input())

needed_money = 0
for year in range(1800, end_year + 1):
    if year % 2 == 0:
        needed_money += 12_000
    else:
        needed_money += 12_000 + (50 * (year - 1782))

diff = abs(money - needed_money)

if money >= needed_money:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')

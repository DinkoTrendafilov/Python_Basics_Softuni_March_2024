import math

number_of_magn = int(input())
number_of_zumb = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
gift_price = float(input())

total_money = (number_of_zumb * 4) + (number_of_magn * 3.25) + (number_of_roses * 3.5) + (number_of_cactus * 8)
total_money *= 0.95

diff = abs(total_money - gift_price)

if gift_price > total_money:
    print(f'She will have to borrow {math.ceil(diff)} leva.')
else:
    print(f'She is left with {math.floor(diff)} leva.')

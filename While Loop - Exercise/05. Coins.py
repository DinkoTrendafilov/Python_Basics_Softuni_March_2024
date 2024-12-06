money = float(input())

coins = 0

money_left = money

while money_left > 0:

    if money_left >= 2:
       money_left -= 2
       coins += 1

    elif money_left >= 1:
       money_left -= 1
       coins += 1

    elif money_left >= 0.5:
       money_left -= 0.5
       coins += 1

    elif money_left >= 0.2:
       money_left -= 0.2
       coins += 1

    elif money_left >= 0.1:
       money_left -= 0.1
       coins += 1

    elif money_left >= 0.05:
       money_left -= 0.05
       coins += 1

    elif money_left >= 0.02:
       money_left -= 0.02
       coins += 1

    elif money_left >= 0.01:
       money_left -= 0.01
       coins += 1

    money_left = round(money_left, 2)

print(coins)
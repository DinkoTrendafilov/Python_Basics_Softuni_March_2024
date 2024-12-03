
MONEY_INCREASE = 10
BROTHER_TAX = 1

years = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_given = 10
money_from_gifts = 0
toys_count = 0


for age  in range(1, years +1):
    if age % 2 == 0:
        money_from_gifts += money_given - BROTHER_TAX
        money_given += MONEY_INCREASE
    else:
        toys_count += 1
total_toy_price = toys_count * toy_price

total_money = money_from_gifts + total_toy_price
diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
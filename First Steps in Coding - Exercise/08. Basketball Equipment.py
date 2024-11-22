annual_tax_for_basketball = int(input())

shoes = annual_tax_for_basketball * 0.6
clothing = shoes * 0.8
ball = clothing / 4
accessories = ball / 5

total_costs = annual_tax_for_basketball + shoes + clothing + ball + accessories

print(f'{total_costs:.2f}')

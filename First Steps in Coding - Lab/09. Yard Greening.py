meters_for_paint = float(input())

price_per_meter = 7.61
discount = 18

costs = meters_for_paint * price_per_meter
discount_price = (costs * discount) / 100

total_costs = costs - discount_price

print(f"The final price is: {total_costs:.2f} lv.")
print(f"The discount is: {discount_price:.2f} lv.")
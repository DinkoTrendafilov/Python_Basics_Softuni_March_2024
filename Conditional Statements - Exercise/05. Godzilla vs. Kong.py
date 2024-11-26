budget = float(input())
count_of_statists = int(input())
price_per_one_dress_of_statists = float(input())

decor = budget * 0.1
total_price_for_statists = count_of_statists * price_per_one_dress_of_statists

if count_of_statists > 150:
    total_price_for_statists -= total_price_for_statists * 0.1

total_costs = decor + total_price_for_statists
diff = abs(budget - total_costs)

if total_costs > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
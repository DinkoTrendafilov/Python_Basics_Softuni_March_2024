budget = float(input())
type_category = input()
people_count = int(input())

vip = 499.99
normal = 249.99

total_costs = 0
transport_costs = 0

if 1 <= people_count <= 4:
    transport_costs = 0.75 * budget
elif 5 <= people_count <= 9:
    transport_costs = 0.6 * budget
elif 10 <= people_count <= 24:
    transport_costs = 0.5 * budget
elif 25 <= people_count <= 49:
    transport_costs = 0.4 * budget
elif people_count >= 50:
    transport_costs = 0.25 * budget

budget -= transport_costs

if type_category == 'VIP':
    budget -= vip * people_count
elif type_category == 'Normal':
    budget -= normal * people_count


if budget >= 0:
    print(f"Yes! You have {budget:.2f} leva left.")
else:
    budget = abs(budget)
    print(f"Not enough money! You need {budget:.2f} leva.")

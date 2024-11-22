needed_quantity_nylon = int(input())
needed_quantity_paint = int(input())
needed_quantity_thinner = int(input())
hours_for_masters = int(input())

nylon_per_single = 1.5
paint_per_single = 14.50
thinner_per_single = 5
back_per_single = 0.4

nylon = (needed_quantity_nylon + 2) * nylon_per_single
paint = (needed_quantity_paint * 1.1) * paint_per_single
thinner = needed_quantity_thinner * thinner_per_single
costs = nylon + paint + thinner + back_per_single

sum_for_masters = (costs * 0.3) * hours_for_masters
total_costs = costs + sum_for_masters
print(f'{total_costs:.2f}')

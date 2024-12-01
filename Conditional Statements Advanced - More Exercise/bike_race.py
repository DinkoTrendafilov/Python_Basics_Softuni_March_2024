count_of_juniors = int(input())
count_of_seniors = int(input())
type_trace = input()

total_costs = 0

if type_trace == 'trail':
    total_costs = (count_of_juniors * 5.5) + (count_of_seniors * 7)
elif type_trace == 'cross-country':
    total_costs = (count_of_juniors * 8) + (count_of_seniors * 9.5)
elif type_trace == 'downhill':
    total_costs = (count_of_juniors * 12.25) + (count_of_seniors * 13.75)
elif type_trace == 'road':
    total_costs = (count_of_juniors * 20) + (count_of_seniors * 21.5)

if type_trace == 'cross-country' and count_of_seniors + count_of_juniors >= 50:
    total_costs *= 0.75

donated_amount = total_costs * 0.95

print(f"{donated_amount:.2f}")

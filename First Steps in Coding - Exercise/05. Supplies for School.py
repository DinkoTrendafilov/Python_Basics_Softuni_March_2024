quantity_pens = int(input())
quantity_markers = int(input())
preparation_in_liters = int(input())
percent_discount = int(input())

sum_of_things = (quantity_pens * 5.8) + (quantity_markers * 7.2) + (preparation_in_liters * 1.2)
discount = (percent_discount * sum_of_things) / 100

total_sum = sum_of_things - discount

print(f'{total_sum:.2f}')

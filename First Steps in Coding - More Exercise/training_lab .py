length_in_meters = float(input())
width_in_meters = float(input())

length_in_sm = length_in_meters * 100
width_in_sm = width_in_meters * 100

rows_in_width = (width_in_sm - 100) // 70
rows_in_length = length_in_sm // 120

total_rows = (rows_in_length * rows_in_width) - 3

print(total_rows)

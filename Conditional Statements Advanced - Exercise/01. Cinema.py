screening_type = input()
rows = int(input())
columns = int(input())

ticket_price = 0
all_seats = rows * columns

if screening_type == 'Premiere':
    ticket_price = 12
elif screening_type == 'Normal':
    ticket_price = 7.5
elif screening_type == 'Discount':
    ticket_price = 5

total_price = ticket_price * all_seats

print(f'{total_price:.2f} leva')

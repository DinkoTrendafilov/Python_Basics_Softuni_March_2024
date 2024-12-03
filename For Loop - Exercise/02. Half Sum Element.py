import sys

n= int(input())

max_number = - sys.maxsize
sum_numbers = 0

for _ in range (0, n):
    number = int (input())

    if number > max_number:
        max_number = number

    sum_numbers += number

if max_number == sum_numbers - max_number:
    print('Yes')
    print(f'Sum = {max_number}')

else:
    diff = abs(max_number - (sum_numbers - max_number))
    print('No')
    print(f'Diff = {diff}')


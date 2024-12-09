number = int(input())
result = 0
avg = 0

for num in range(1, number + 1):
    current_number = int(input())
    result += current_number
    avg = result / number

print(f'{avg:.2f}')

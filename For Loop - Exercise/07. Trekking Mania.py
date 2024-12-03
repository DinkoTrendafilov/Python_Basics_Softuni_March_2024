n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

total_persons = 0

for _ in range(n):
    num = int(input())

    if num <= 5:
        p1 += num

    elif num <= 12:
        p2 += num

    elif num <= 25:
        p3 += num

    elif num <= 40:
        p4 += num

    elif num >= 41:
        p5 += num

    total_persons += num


print(f'{(p1/total_persons * 100):.2f}%')
print(f'{(p2/total_persons * 100):.2f}%')
print(f'{(p3/total_persons * 100):.2f}%')
print(f'{(p4/total_persons * 100):.2f}%')
print(f'{(p5/total_persons * 100):.2f}%')


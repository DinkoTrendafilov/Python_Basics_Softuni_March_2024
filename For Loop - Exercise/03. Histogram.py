n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0


for _ in range (0, n):

    num = int(input())
    if num < 200:
        p1 += 1
    elif num >= 200 and num < 400:
        p2 += 1
    elif num >= 400 and num < 600:
        p3 += 1
    elif num >= 600 and num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1

total_numbers = p1 + p2 + p3 + p4 + p5

print(f'{(p1 * 100 )/ total_numbers:.2f}%')
print(f'{(p2 * 100 )/ total_numbers:.2f}%')
print(f'{(p3 * 100 )/ total_numbers:.2f}%')
print(f'{(p4 * 100 )/ total_numbers:.2f}%')
print(f'{(p5 * 100 )/ total_numbers:.2f}%')
import math

command = input()

if command == 'square':
    side = float(input())
    area = side * side
elif command == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
elif command == 'circle':
    radius = float(input())
    area = math.pi * radius * radius
elif command == 'triangle':
    side1 = float(input())
    side2 = float(input())
    area = (side1 * side2) / 2

print(f'{area:.3f}')
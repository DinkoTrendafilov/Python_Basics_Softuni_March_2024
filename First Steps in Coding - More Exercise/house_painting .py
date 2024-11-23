x = float(input())
y = float(input())
h = float(input())

# walls
side_wall = x * y
windows = 1.5 * 1.5
two_pages = (2 * side_wall) - (2 * windows)
back_wall = x * x
entrance = 1.2 * 2
total_side_and_back_wall = (2 * back_wall) - entrance
total_area = two_pages + total_side_and_back_wall
green_paint = total_area / 3.4

# roof
two_rectangles = 2 * (x * y)
two_triangles = 2 * (x * h) / 2
total_area_1 = two_rectangles + two_triangles
red_paint = total_area_1 / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')



length = int(input())
weight = int(input())
hight = int(input())

total_space = length * weight * hight
is_free_space_enough = True
while True:
    command = input()
    if command == 'Done':
        break
    cartons =  int(command)
    total_space -= cartons
    if total_space < 0:
        is_free_space_enough = False
        break

diff = abs(total_space)
if is_free_space_enough:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")


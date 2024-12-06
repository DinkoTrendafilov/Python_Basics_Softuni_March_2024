hight = int(input())
weight = int(input())

is_finished = False
whole_pieces = hight * weight

while True:
    command = input()
    if command == 'STOP':
        break
    pieces = int(command)
    whole_pieces -= pieces

    if whole_pieces < 0:
        is_finished = True
        break


diff = abs(whole_pieces)
if not is_finished:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")


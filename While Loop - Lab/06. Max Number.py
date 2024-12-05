import sys

max_number = -sys.maxsize

while True:
    command = input()
    if command == 'Stop':
        print(max_number)
        break
    number = int(command)
    if number > max_number:
        max_number = number
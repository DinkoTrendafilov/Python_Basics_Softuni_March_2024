import sys

min_number = sys.maxsize

while True:
    command = input()
    if command == 'Stop':
        print(min_number)
        break
    number = int(command)
    if number < min_number:
        min_number = number
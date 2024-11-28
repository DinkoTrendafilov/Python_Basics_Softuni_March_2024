product = input()
day = input()
quantity = float(input())
is_valid = False
result = 0

if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    if product == 'banana':
        result = 2.5 * quantity
    elif product == 'apple':
        result = 1.2 * quantity
    elif product == 'orange':
        result = 0.85 * quantity
    elif product == 'grapefruit':
        result = 1.45 * quantity
    elif product == 'kiwi':
        result = 2.7 * quantity
    elif product == 'pineapple':
        result = 5.5 * quantity
    elif product == 'grapes':
        result = 3.85 * quantity
    else:
        is_valid = True


elif day in ('Saturday', 'Sunday'):
    if product == 'banana':
        result = 2.7 * quantity
    elif product == 'apple':
        result = 1.25 * quantity
    elif product == 'orange':
        result = 0.9 * quantity
    elif product == 'grapefruit':
        result = 1.6 * quantity
    elif product == 'kiwi':
        result = 3 * quantity
    elif product == 'pineapple':
        result = 5.6 * quantity
    elif product == 'grapes':
        result = 4.2 * quantity
    else:
        is_valid = True
else:
    is_valid = True


if is_valid:
    print('error')
else:
    print(f'{result:.2f}')
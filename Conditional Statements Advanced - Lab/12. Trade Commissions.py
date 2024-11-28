town = input()
sales = float(input())
is_valid = True
percent_discount = 0

if town == 'Sofia':
    if 0 <= sales <= 500:
        percent_discount = 5
    elif sales <= 1000:
        percent_discount = 7
    elif sales <= 10_000:
        percent_discount = 8
    elif sales > 10_000:
        percent_discount = 12
    else:
        is_valid = False


elif town == 'Varna':
    if 0 <= sales <= 500:
        percent_discount = 4.5
    elif sales <= 1000:
        percent_discount = 7.5
    elif sales <= 10_000:
        percent_discount = 10
    elif sales > 10_000:
        percent_discount = 13
    else:
        is_valid = False


elif town == 'Plovdiv':
    if 0 <= sales <= 500:
        percent_discount = 5.5
    elif sales <= 1000:
        percent_discount = 8
    elif sales <= 10_000:
        percent_discount = 12
    elif sales > 10_000:
        percent_discount = 14.5
    else:
        is_valid = False

else:
    is_valid = False

price = sales * percent_discount / 100

if is_valid:
    if price < 0:
        print('error')
    else:
        print(f'{price:.2f}')
else:
    print('error')

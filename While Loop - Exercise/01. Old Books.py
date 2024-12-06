target_book = input()
counter_book = 0
is_found_book = False

while True:

    current_book = input()

    if current_book == 'No More Books':
        break
    elif current_book == target_book:
        is_found_book = True
        break

    counter_book += 1

if is_found_book:
    print(f'You checked {counter_book} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter_book} books.')



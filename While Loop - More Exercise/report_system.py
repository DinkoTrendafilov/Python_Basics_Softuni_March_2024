needed_sum = int(input())

payment_cash = 0
cash_counter = 0

payment_cards = 0
cards_counter = 0

collected_sum = 0
counter = 0

while True:
    command = input()
    if command == 'End':
        print('Failed to collect required money for charity.')
        break
    current_sum = int(command)
    counter += 1
    if counter % 2 == 1:
        if current_sum > 100:
            print("Error in transaction!")
            continue
        else:
            print("Product sold!")
        payment_cash += current_sum
        cash_counter += 1

    else:
        if current_sum < 10:
            print("Error in transaction!")
            continue
        else:
            print("Product sold!")
        payment_cards += current_sum
        cards_counter += 1

    collected_sum += current_sum
    if collected_sum >= needed_sum:
        avg_cash = payment_cash / cash_counter
        avg_cards = payment_cards / cards_counter
        print(f'Average CS: {avg_cash:.2f}')
        print(f'Average CC: {avg_cards:.2f}')
        break

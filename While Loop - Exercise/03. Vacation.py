needed_money = float(input())
money_in_hand = float(input())

total_days_counter = 0
spend_counter = 0
is_spending_too_many_days_in_row = False

while True:
    if money_in_hand >= needed_money:
        break
    action = input()
    current_sum = float(input())

    total_days_counter += 1

    if action == 'spend':
        spend_counter += 1
        if spend_counter == 5:
            is_spending_too_many_days_in_row = True
            break
        money_in_hand -= current_sum
        if money_in_hand < 0:
            money_in_hand = 0
    elif action == 'save':
        money_in_hand += current_sum
        spend_counter = 0

if is_spending_too_many_days_in_row:
    print("You can't save the money.")
    print(f'{total_days_counter}')
else:
    print(f'You saved the money for {total_days_counter} days.')

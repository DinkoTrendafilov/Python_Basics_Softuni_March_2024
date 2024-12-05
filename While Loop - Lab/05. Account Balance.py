total_sum = 0
while True:
    command = input()
    if command == 'NoMoreMoney':
        print(f'Total: {total_sum:.2f}')
        break
    money = float(command)
    if money < 0:
        print('Invalid operation!')
        print(f'Total: {total_sum:.2f}')
        break
    else:
        print(f'Increase: {money:.2f}')
    total_sum += money
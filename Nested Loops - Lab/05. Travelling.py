while True:
    command = input()
    if command == 'End':
        break
    destination = command
    needed_money = float(input())
    current_money = 0
    while True:
        if current_money >= needed_money:
            break
        saved_money = float(input())
        current_money += saved_money

    print(f"Going to {destination}!")

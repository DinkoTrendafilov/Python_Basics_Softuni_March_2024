first_enter_number = int(input())
last_enter_number = int(input())
magic_number = int(input())

combination_found = False
counter = 0
for num1 in range(first_enter_number, last_enter_number + 1):
    for num2 in range(first_enter_number, last_enter_number + 1):
        counter += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_number})")
            combination_found = True
            break

    if combination_found:
        break


if not combination_found:
    print(f"{counter} combinations - neither equals {magic_number}")

prime_members_sum = 0
non_prime_members_sum = 0
while True:
    command = input()
    if command == 'stop':
        break
    number = int(command)

    if number < 0:
        print('Number is negative.')

    else:
        is_prime_number = True
        for num in range(2, number):
            if number % num == 0:
                is_prime_number = False
                break

        if is_prime_number:
            prime_members_sum += number
        else:
            non_prime_members_sum += number

print(f"Sum of all prime numbers is: {prime_members_sum}")
print(f"Sum of all non prime numbers is: {non_prime_members_sum}")

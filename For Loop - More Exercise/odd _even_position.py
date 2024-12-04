OddSum = 'No'
OddMin = 'No'
OddMax = 'No'
EvenSum = 'No'
EvenMin = 'No'
EvenMax = 'No'
n = int(input())
if n > 0:
    number = float(input())
num = 1

if n == 0:
    OddSum = 0
    EvenSum = 0
elif n == 1:
    OddSum = number
    OddMin = number
    OddMax = number
    EvenSum = 0
elif n > 1:

    while num <= n:

        # odd
        if num % 2 != 0:
            if OddSum == 'No':
                OddSum = number
            elif OddSum != 'No':
                OddSum += number

            if OddMin == 'No':
                OddMin = number
            elif OddMin != 'No':
                if number < OddMin:
                    OddMin = number

            if OddMax == 'No':
                OddMax = number
            elif OddMax != 'No':
                if number > OddMax:
                    OddMax = number

        # even
        elif num % 2 == 0:
            if EvenSum == 'No':
                EvenSum = number
            elif EvenSum != 'No':
                EvenSum += number

            if EvenMin == 'No':
                EvenMin = number
            elif EvenMin != 'No':
                if number < EvenMin:
                    EvenMin = number

            if EvenMax == 'No':
                EvenMax = number
            elif EvenMax != 'No':
                if number > EvenMax:
                    EvenMax = number

        num += 1
        if num > n:
            break
        number = float(input())

if OddSum == 'No':
    print(f"OddSum={OddSum},")
elif OddSum != 'No':
    print(f"OddSum={OddSum:.2f},")

if OddMin == 'No':
    print(f"OddMin={OddMin},")
elif OddMin != 'No':
    print(f"OddMin={OddMin:.2f},")

if OddMax == 'No':
    print(f"OddMax={OddMax},")
elif OddMax != 'No':
    print(f"OddMax={OddMax:.2f},")

if EvenSum == 'No':
    print(f"EvenSum={EvenSum},")
elif EvenSum != 'No':
    print(f"EvenSum={EvenSum:.2f},")

if EvenMin == 'No':
    print(f"EvenMin={EvenMin},")
elif EvenMin != 'No':
    print(f"EvenMin={EvenMin:.2f},")

if EvenMax == 'No':
    print(f"EvenMax={EvenMax}")
elif EvenMax != 'No':
    print(f"EvenMax={EvenMax:.2f}")
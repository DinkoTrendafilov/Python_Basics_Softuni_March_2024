
number_of_open_tabs = int(input())
salary = int(input())


for tabs in range(1, number_of_open_tabs + 1):
    open_tabs = input()

    if open_tabs == 'Facebook':
        salary -= 150
    elif open_tabs == 'Instagram':
        salary -= 100
    elif open_tabs == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break


else:
    print(salary)

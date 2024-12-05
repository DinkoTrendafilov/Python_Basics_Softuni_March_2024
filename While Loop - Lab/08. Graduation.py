name_of_student = input()
negative_counter = 0
sum_of_grades = 0
counter_of_classes = 0

while counter_of_classes < 12:
    grade = float(input())

    if grade < 4:
        negative_counter += 1
        if negative_counter == 2:
            print(f'{name_of_student} has been excluded at {counter_of_classes + 1} grade')
            break

        continue
    counter_of_classes += 1
    sum_of_grades += grade

else:
    average_grade = sum_of_grades / 12
    print(f'{name_of_student} graduated. Average grade: {average_grade:.2f}')

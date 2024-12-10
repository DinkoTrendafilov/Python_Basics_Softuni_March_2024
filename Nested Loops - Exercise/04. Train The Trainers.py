number_of_jury = int(input())
final_grade = 0
presentation_grades_count = 0

while True:
    command = input()
    if command == 'Finish':
        break
    presentation_name = command
    current_presentation_grade = 0

    for grade in range(number_of_jury):
        current_grade = float(input())
        current_presentation_grade += current_grade
        presentation_grades_count += 1

    current_presentation_grades_average = current_presentation_grade / number_of_jury
    print(f"{presentation_name} - {current_presentation_grades_average:.2f}.")
    final_grade += current_presentation_grade


final_grade /= presentation_grades_count
print(f"Student's final assessment is {final_grade:.2f}.")


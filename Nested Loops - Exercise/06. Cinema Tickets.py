student_tickets_count = 0
kid_tickets_count = 0
standard_tickets_count = 0

while True:
    command = input()
    if command == 'Finish':
        is_finish = True
        break
    name_of_movie = command
    free_seats_on_cinema = int(input())
    sold_tickets = 0

    for ticket in range(free_seats_on_cinema):
        current_ticket = input()
        if current_ticket == 'End':
            break
        elif current_ticket == 'kid':
            kid_tickets_count += 1
        elif current_ticket == 'student':
            student_tickets_count += 1
        elif current_ticket == 'standard':
            standard_tickets_count += 1
        sold_tickets += 1
    print(f"{name_of_movie} - {(sold_tickets / free_seats_on_cinema * 100):.2f}% full.")

total_tickets = standard_tickets_count + kid_tickets_count + student_tickets_count

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets_count / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets_count / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid_tickets_count / total_tickets) * 100:.2f}% kids tickets.")

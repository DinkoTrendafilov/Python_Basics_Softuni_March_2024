count_pages = int(input())
pages_for_one_hour = int(input())
count_of_days = int(input())

total_time_for_book = count_pages // pages_for_one_hour
necessary_days_for_book = total_time_for_book / count_of_days

print(necessary_days_for_book)
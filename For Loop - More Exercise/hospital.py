period_in_days = int(input())

treated_patients = 0
untreated_patients = 0
doctors_count = 7

for day in range(1, period_in_days + 1):
    number_of_patients = int(input())
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors_count += 1
    if number_of_patients > doctors_count:
        untreated_patients += number_of_patients - doctors_count
        treated_patients += doctors_count
    else:
        treated_patients += number_of_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

period_days = int(input())
doctor_number = 7
total_treated_patients = 0
total_untreated_patients = 0

for i in range(1, period_days + 1):
    daily_treated_patients = 0
    daily_untreated_patients = 0

    if i % 3 == 0 and total_untreated_patients > total_treated_patients:
        doctor_number += 1
    patients_count = int(input())

    if doctor_number >= patients_count:
        daily_treated_patients = patients_count
        daily_untreated_patients = 0
    if doctor_number < patients_count:
        daily_untreated_patients = patients_count - doctor_number
        daily_treated_patients = patients_count - daily_untreated_patients

    total_treated_patients += daily_treated_patients
    total_untreated_patients += daily_untreated_patients

print(f'Treated patients: {total_treated_patients}.')
print(f'Untreated patients: {total_untreated_patients}.')

sleep_needed = 30000
time_spent_workdays = 63
time_spent_holydays = 127

holydays = int(input())
workdays = 365 - holydays

total_time_spent = (workdays * time_spent_workdays) + (holydays * time_spent_holydays)

h = abs(sleep_needed - total_time_spent) // 60
m = abs(sleep_needed - total_time_spent) % 60

if total_time_spent <= sleep_needed:
    print(f"Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")

else:
    print(f"Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
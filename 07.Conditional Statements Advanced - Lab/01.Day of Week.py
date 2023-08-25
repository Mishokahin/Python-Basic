daysOfTheWeek = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

n = int(input())

if n in daysOfTheWeek:
    print(daysOfTheWeek[n])
else:
    print("Error")
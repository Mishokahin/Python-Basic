workdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

hour = int(input())
day = input().lower()

if day in workdays:
    if hour in range(10, 19):
        print("open")
    else:
        print("closed")
else:
    print("closed")
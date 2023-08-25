workdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["saturday", "sunday"]
request = input()

if request.lower() in workdays:
    print("Working day")
elif request.lower() in weekend:
    print("Weekend")
else:
    print("Error")

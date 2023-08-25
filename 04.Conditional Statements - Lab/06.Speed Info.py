i = float(input())

if i <= 10:
    print("slow")
elif i <= 50:
    print("average")
elif i <= 150:
    print("fast")
elif i <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
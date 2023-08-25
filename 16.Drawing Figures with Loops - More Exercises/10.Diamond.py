n = int(input())

if n == 1:
    print("*")
elif n == 2:
    print("**")
elif n % 2 == 0:
    num = []
    for i in range(int(n / 2) - 1, 0, -1):
        num.append(i)
    for f in range(int(n / 2) - 1):
        if f == 0:
            print((num[f] * "-") + "**" + (num[f] * "-"))
        else:
            print((num[f] * "-") + "*" + (f * 2) * "-" + "*" + (num[f] * "-"))
    print("*" + ((n - 2) * "-") + "*")
    for f in range(int(n / 2) - 2, -1, -1):
        if f == 0:
            print((num[f] * "-") + "**" + (num[f] * "-"))
        else:
            print((num[f] * "-") + "*" + (f * 2) * "-" + "*" + (num[f] * "-"))
else:
    num = []
    for i in range(int(n / 2), 0, -1):
        num.append(i)
    for f in range(int(n/2)):
        if f == 0:
            print((num[f] * "-") + "*" + (num[f] * "-"))
        else:
            print((num[f] * "-") + "*" + ((f*2)-1) * "-" + "*" + (num[f] * "-"))
    print("*" + ((n-2) * "-") + "*")
    for f in range(int(n/2)-1, -1, -1):
        if f == 0:
            print((num[f] * "-") + "*" + (num[f] * "-"))
        else:
            print((num[f] * "-") + "*" + ((f * 2) - 1) * "-" + "*" + (num[f] * "-"))
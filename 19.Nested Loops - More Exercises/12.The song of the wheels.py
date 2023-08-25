M = int(input())
passwords = [f"{a}{b}{c}{d}"
             for a in range(1, 10)
             for b in range(1, 10)
             for c in range(1, 10)
             for d in range(1, 10)
             if a < b and c > d and (a*b) + (c*d) == M]

if len(passwords) == 0:
    print("No!")
elif len(passwords) < 4:
    print(*passwords, "\nNo!")
else:
    print(*passwords, f"\nPassword: {passwords[3]}")
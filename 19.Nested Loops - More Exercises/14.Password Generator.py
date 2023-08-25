import string
n = int(input())
l = int(input())
letters = string.ascii_lowercase

passwords = [f"{a}{b}{letters[l1]}{letters[l2]}{c}"
             for a in range(1, n+1)
             for b in range(1, n+1)
             for l1 in range(l)
             for l2 in range(l)
             for c in range(1, n+1)
             if c > a and c > b]

print(*passwords)
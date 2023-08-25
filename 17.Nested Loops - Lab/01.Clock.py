clock = [f"{h}:{m}"
         for h in range(24)
         for m in range(60)
         ]
print(*clock, sep="\n")
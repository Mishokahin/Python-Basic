one_count = int(input())
two_count = int(input())
five_count = int(input())
target = int(input())

profit = [f"\n{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {target} lv."
          for one in range(one_count+1)
          for two in range(two_count+1)
          for five in range(five_count+1)
          if (one * 1) + (two * 2) + (five * 5) == target
          ]

print(*profit, sep="\n")
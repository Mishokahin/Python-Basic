w = float(input())
h = float(input())

hall_width = (w * 100)
hall_height = (h * 100) - 100

desks_in_row = int(hall_height/70)
rows = int(hall_width/120)

print((desks_in_row * rows)-3)

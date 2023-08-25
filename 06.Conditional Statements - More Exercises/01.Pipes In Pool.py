v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

volume_filled = (p1 * h) + (p2 * h)

if volume_filled <= v:
    print(f"The pool is {(volume_filled/v)*100:.2f}% full. Pipe 1: {((p1 * h)/volume_filled)*100:.2f}%. Pipe 2: {((p2 * h)/volume_filled)*100:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {abs(volume_filled - v):.2f} liters.")
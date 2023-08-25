x = float(input())
y = float(input())
h = float(input())

green_paint = 3.4
red_paint = 4.3

sides = ((x*y)*2) - (2*(1.5*1.5))
front_back = (2*(x*x)) - 2.4

roof_side = 2* (x*y)
roof_triangles = 2 * (x*h/2)

print(f"{(sides + front_back) / green_paint:.2f}")
print(f"{(roof_side + roof_triangles) / red_paint:.2f}")
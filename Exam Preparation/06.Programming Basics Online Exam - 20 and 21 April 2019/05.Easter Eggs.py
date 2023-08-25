number_of_eggs = int(input())
color = [input() for i in range(number_of_eggs)]
colors = {"red": len([x for x in color if x == "red"]),
          "orange": len([x for x in color if x == "orange"]),
          "blue": len([x for x in color if x == "blue"]),
          "green": len([x for x in color if x == "green"])
          }

print(f"Red eggs: {colors['red']}")
print(f"Orange eggs: {colors['orange']}")
print(f"Blue eggs: {colors['blue']}")
print(f"Green eggs: {colors['green']}")
print(f"Max eggs: {max(colors.values())} -> {max(colors, key=colors.get)}")
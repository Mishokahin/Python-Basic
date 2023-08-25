multiplication_table = [f"{x} * {y} = {x * y}"
                        for x in range(1, 11)
                        for y in range(1, 11)
                        ]
print(*multiplication_table, sep="\n")
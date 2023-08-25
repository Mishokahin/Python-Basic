n1 = [i for i in input()]
n2 = [i for i in input()]

barcodes = [f"{i}{j}{k}{l}"
            for i in range(int(n1[0]), int(n2[0])+1) if i % 2 != 0
            for j in range(int(n1[1]), int(n2[1])+1) if j % 2 != 0
            for k in range(int(n1[2]), int(n2[2])+1) if k % 2 != 0
            for l in range(int(n1[3]), int(n2[3])+1) if l % 2 != 0
            ]

print(*barcodes, sep=" ")
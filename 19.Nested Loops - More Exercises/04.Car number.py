n1 = int(input())
n2 = int(input())

car_number = [f"{i}{j}{k}{l}"
              for i in range(n1, n2+1)
              for j in range(n1, n2+1)
              for k in range(n1, n2+1)
              for l in range(n1, n2+1)
              if ((i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0)) and i > l and (j + k) % 2 == 0]

print(*car_number)
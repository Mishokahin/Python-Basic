prices = {"John Wick": {"Drink": 12, "Popcorn": 15, "Menu": 19},
          "Star Wars": {"Drink": 18, "Popcorn": 25, "Menu": 30},
          "Jumanji": {"Drink": 9, "Popcorn": 11, "Menu": 14}
          }

movie = input()
package = input()
tickets = int(input())
total = 0

if movie in prices:
    if package in prices[movie]:
        if movie == "Star Wars" and tickets >= 4:
            total = (tickets * prices[movie][package]) * (1 - 0.3)
        elif movie == "Jumanji" and tickets == 2:
            total = (tickets * prices[movie][package]) * (1 - 0.15)
        else:
            total = tickets * prices[movie][package]

print(f"Your bill is {total:.2f} leva.")
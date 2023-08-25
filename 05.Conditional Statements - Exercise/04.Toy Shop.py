vacation = float(input())
puzzles = int(input())
talkingDolls = int(input())
teddyBears = int(input())
minions = int(input())
trucks = int(input())

itemsSold = puzzles + talkingDolls + teddyBears + minions + trucks
totalPriceOfItems = (puzzles * 2.6) + (talkingDolls * 3) + (teddyBears * 4.1) + (minions * 8.2) + (trucks * 2)
profit = totalPriceOfItems - (totalPriceOfItems * 0.1)

if itemsSold >= 50:
    totalPriceOfItems -= totalPriceOfItems * 0.25

if totalPriceOfItems - (totalPriceOfItems * 0.1) >= vacation:
    print(f"Yes! {totalPriceOfItems- (totalPriceOfItems * 0.1)- vacation:.2f} lv left.")

else:
    print(f"Not enough money! {vacation - (totalPriceOfItems- (totalPriceOfItems * 0.1)):.2f} lv needed.")

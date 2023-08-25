yardSqM = float(input())
priceOfWork = yardSqM * 7.61
discount = priceOfWork * 0.18
totalPrice = priceOfWork - discount

print(f"The final price is: {totalPrice} lv.")
print(f"The discount is: {discount} lv.")
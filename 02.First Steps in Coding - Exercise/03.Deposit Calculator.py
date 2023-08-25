depositAmount = float(input())
depositLength = int(input())
yearlyInterestRate = float(input())/100

print(depositAmount + depositLength * ((depositAmount * yearlyInterestRate)/12))

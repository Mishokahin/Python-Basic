import math

currentRecord = float(input())
distance = float(input())
secondsPerMeter = float(input())

waterResistance = math.floor(distance / 15) * 12.5
totalTime = (distance * secondsPerMeter) + waterResistance


if totalTime < currentRecord:
    print(f"Yes, he succeeded! The new world record is {totalTime:.2f} seconds.")

else:
    print(f"No, he failed! He was {abs(currentRecord - totalTime):.2f} seconds slower.")
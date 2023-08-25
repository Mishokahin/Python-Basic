import math

seriesName = input()
episodeLength = int(input())
lunchBreak = int(input())

timeToEat = lunchBreak / 8
timeToRest = lunchBreak / 4
timeLeft = lunchBreak - timeToEat - timeToRest


if timeLeft >= episodeLength:
    print(f"You have enough time to watch {seriesName} and left with {math.ceil(timeLeft - episodeLength)} minutes free time.")

else:
    print(f"You don't have enough time to watch {seriesName}, you need {math.ceil(episodeLength - timeLeft)} more minutes.")
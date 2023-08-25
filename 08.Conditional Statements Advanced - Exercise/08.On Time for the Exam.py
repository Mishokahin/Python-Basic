examStartHour = int(input())
examStartMinutes = int(input())
studentArrivalHour = int(input())
studentArrivalMinutes = int(input())

totalExamTime = (examStartHour * 60) + examStartMinutes
totalArrivalTime = (studentArrivalHour * 60) + studentArrivalMinutes

timeDifference = abs(totalExamTime - totalArrivalTime)

if totalArrivalTime == totalExamTime:
    print("On time")

elif totalArrivalTime < totalExamTime:
    if timeDifference <= 30:
        print("On time")
        print(f"{timeDifference} minutes before the start")

    else:
        if timeDifference >= 60:
            hh = timeDifference // 60
            mm = timeDifference % 60
            if mm < 10:
                print("Early")
                print(f"{hh}:0{mm} hours before the start")
            else:
                print("Early")
                print(f"{hh}:{mm} hours before the start")
        else:
            print("Early")
            print(f"{timeDifference} minutes before the start")

elif totalArrivalTime > totalExamTime:
    print("Late")
    if timeDifference >= 60:
        hh = timeDifference // 60
        mm = timeDifference % 60
        if mm < 10:
            print(f"{hh}:0{mm} hours after the start")
        else:
            print(f"{hh}:{mm} hours after the start")
    else:
        print(f"{timeDifference} minutes after the start")
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

difference = arrival_time - exam_time

if difference > 0:
    print("Late")
elif difference >= -30:
    print("On time")
else:
    print("Early")

if difference != 0:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60

    if hours == 0:
        if difference < 0:
            print(f"{minutes} minutes before the start")
        else:
            print(f"{minutes} minutes after the start")
    else:
        if difference < 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{hours}:{minutes:02d} hours after the start")
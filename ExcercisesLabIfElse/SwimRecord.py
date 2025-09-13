record = float(input())
meters = float(input())
time_per_meter = float(input())

swim_time = meters * time_per_meter

delay = (meters // 15) * 12.5

total_time = swim_time + delay

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")
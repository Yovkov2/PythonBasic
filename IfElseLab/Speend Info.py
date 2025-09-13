speed_info = float(input())

if speed_info <= 10:
    print("slow")
elif speed_info > 10 and speed_info <= 50:
    print("average")
elif speed_info > 50 and speed_info <= 150:
    print("fast")
elif speed_info > 150 and speed_info <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
film = input()
sector = input()
tickets_count = int(input())
sum = 0

if film == "A Star Is Born":
    if sector == "normal":
        sum = tickets_count * 7.50
    elif sector == "luxury":
        sum = tickets_count * 10.50
    elif sector == "ultra luxury":
        sum = tickets_count * 13.50
elif film == "Bohemian Rhapsody":
    if sector == "normal":
        sum = tickets_count * 7.35
    elif sector == "luxury":
        sum = tickets_count * 9.45
    elif sector == "ultra luxury":
        sum = tickets_count * 12.75
elif film == "Green Book":
    if sector == "normal":
        sum = tickets_count * 8.15
    elif sector == "luxury":
        sum = tickets_count * 10.25
    elif sector == "ultra luxury":
        sum = tickets_count * 13.25
elif film == "The Favourite":
    if sector == "normal":
        sum = tickets_count * 8.75
    elif sector == "luxury":
        sum = tickets_count * 11.55
    elif sector == "ultra luxury":
        sum = tickets_count * 13.95


print(f"{film} -> {sum:.2f} lv.")
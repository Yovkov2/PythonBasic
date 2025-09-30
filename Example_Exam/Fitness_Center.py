training_people = int(input())
back = chest = legs = abs = protein_shake = protein_bar = 0
for i in range(1, training_people + 1):
    command = input()
    if command == "Back":
        back += 1
    elif command == "Chest":
        chest += 1
    elif command == "Legs":
        legs += 1
    elif command == "Abs":
        abs += 1
    elif command == "Protein shake":
        protein_shake += 1
    elif command == "Protein bar":
        protein_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
total = training_people
work_out = back + chest + legs + abs
protein = protein_shake + protein_bar
work_out_percent = work_out / total * 100
protein_percent = protein / total * 100

print(f"{work_out_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")

the_book = input()
book = input()
count = 0

while book != "No More Books":
    if book == the_book:
        print(f"You checked {count} books and found it.")
        break
    count += 1
    book = input()
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")

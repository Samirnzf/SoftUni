book_name = input()
checked_books_counter = 0
book_is_found = False
while True:
    current_book = input()
    if current_book == book_name:
        book_is_found = True
        break
    elif current_book == "No More Books":
        break
    checked_books_counter += 1

if book_is_found:
    print(f"You checked {checked_books_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books_counter} books.")

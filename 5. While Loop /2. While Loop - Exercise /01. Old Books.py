import sys

book_needed = input()

book = input()
count_of_books = 0

while book != book_needed:
    if book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {count_of_books} books.')

        sys.exit()

    book = input()
    count_of_books += 1

print(f'You checked {count_of_books} books and found it.')

starting_letter = input()
ending_number = input()
letter_to_ignore = ord(input())

combinations = 0

for i in range(ord(starting_letter), ord(ending_number) + 1):
    for j in range(ord(starting_letter), ord(ending_number) + 1):
        for h in range(ord(starting_letter), ord(ending_number) + 1):
            if i != letter_to_ignore and j != letter_to_ignore and h != letter_to_ignore:
                print(f'{chr(i)}{chr(j)}{chr(h)}', end=" ")
                combinations += 1

print(combinations)

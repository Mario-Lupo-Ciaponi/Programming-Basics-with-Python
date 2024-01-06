word = input()
sum_nouns = 0

for letter in word:
    if letter == 'a':
        sum_nouns += 1
    elif letter == 'e':
        sum_nouns += 2
    elif letter == 'i':
        sum_nouns += 3
    elif letter == 'o':
        sum_nouns += 4
    elif letter == 'u':
        sum_nouns += 5

print(sum_nouns)

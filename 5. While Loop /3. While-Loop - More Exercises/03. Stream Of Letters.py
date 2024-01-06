letter = input()

word = ''
word_to_print = ''

c_count = 0
o_count = 0
n_count = 0

while letter != 'End':
    if letter.isalpha():
        if letter == 'c':
            c_count += 1

            if c_count > 1:
                word += letter
        elif letter == 'o':
            o_count += 1

            if o_count > 1:
                word += letter
        elif letter == 'n':
            n_count += 1

            if n_count > 1:
                word += letter
        else:
            word += letter

        if c_count >= 1 and o_count >= 1 and n_count >= 1:
            c_count = 0
            o_count = 0
            n_count = 0

            word_to_print += word + ' '
            word = ''

    letter = input()

print(word_to_print)

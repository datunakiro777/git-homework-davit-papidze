def is_unique(word):
    is_unique = True
    letter_count = 0
    for i in word:
        for m in word:
            if i == m:
                letter_count += 1
                if letter_count > 1:
                    return 'is not unique', print('is not unique')
        letter_count = 0
    if letter_count == 0:
        return 'is unique', print('is unique')

is_unique('hello')
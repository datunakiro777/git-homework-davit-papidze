def countletters(word):
    letter_dict = {}
    for i in word:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict.update({i : 1})
    return letter_dict, print(letter_dict)

countletters('hello')

x = 'helo'
x[1] = x[2]
print(x[1])

                
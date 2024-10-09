def reverse_word(word):
    word_length = len(word)
    reversed_word = ''
    if word_length % 2 == 0:
        for i in word:
            letter_index = word.index(i)
            letter2_index = 0 - letter_index - 1
            reversed_word += word[letter2_index]
        return reversed_word
    else:
        for i in word:
            letter_index = word.index(i)
            if letter_index + 0.5 == word_length / 2:
                reversed_word += word[letter_index]
            else:
                letter2_index = 0 - letter_index - 1
                reversed_word += word[letter2_index]
        return reversed_word

                
print(reverse_word('hello'))
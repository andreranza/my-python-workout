def pig_latin():
    '''Translate english words to pig latin'''
    eng_word = input('Please, enter a word to be translated into pig latin: ')
    if eng_word[0] in ('a', 'e', 'i', 'o', 'u'):
        pig_word = eng_word + 'way'
    else:
        pig_word = eng_word[1:len(eng_word)] + eng_word[0] + 'ay'
    print(pig_word)

if __name__ == "__main__":
    pig_latin()



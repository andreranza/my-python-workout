import string

def pig_latin(eng_word):
    '''Translate english words to pig latin'''
    if eng_word[0] in 'aeiou':
        pig_word = eng_word + 'way'
    else:
        pig_word = eng_word[1:len(eng_word)] + eng_word[0] + 'ay'
    print(pig_word)

def pig_latin2(word):
    '''Translate english words to pig latin (solution)'''
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

def pig_latin_captalized(word):
    '''Translate english words to pig latin'''

    if word[0].lower() in 'aeiou':
        pig_word = f'{word}way'
    else:   
        pig_word = f'{word[1:]}{word[0]}ay'
    
    if word[0].isupper():
        pig_word = f'{pig_word[0].capitalize()}{pig_word[1:].lower()}'

    return pig_word

def pig_latin_captalized_punctuaction(word):
    '''Translate english words to pig latin, handling both first capital letters
        and final punctuation'''
    word = word.strip()

    if word[-1] in string.punctuation:
        last_punct = word[-1]
        word = word.rstrip(string.punctuation)
    else:
        last_punct = ''

    if word[0].lower() in 'aeiou':
        pig_word = f'{word}way'
    else:   
        pig_word = f'{word[1:]}{word[0]}ay'
    
    if word[0].isupper():
        pig_word = f'{pig_word[0].capitalize()}{pig_word[1:].lower()}'

    return f'{pig_word}{last_punct}'

def alternative_pig_latin(word):
    vowels = set('aeiou')
    n_vowels = len(set(word).intersection(vowels)) # or len(set(word) & set('aeiou'))
    if n_vowels > 1:
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'


if __name__ == "__main__":
    print(pig_latin_captalized_punctuaction('Python!'))
    print(pig_latin_captalized_punctuaction('python@'))
    print(pig_latin_captalized_punctuaction('Abel!'))
    print(alternative_pig_latin('wine'))
    print(alternative_pig_latin('wind'))



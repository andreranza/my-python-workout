import string

def ubbi_dubbi(eng_word):
    """Ask the user to enter a word,
    and return the word's translation into Ubbi Dubbi."""
    ubbi_word = list()
    for letter in eng_word:
        if letter in 'aeiou':
            ubbi_word.append(f'ub{letter}')
        else:
            ubbi_word.append(f'{letter}')
    return ''.join(ubbi_word)

def ubbi_dubbi_capital(eng_word):
    """Ask the user to enter a word,
    and return the word's translation into Ubbi Dubbi."""
    
    ubbi_word = list()
    for letter in eng_word:
        if letter.lower() in 'aeiou':
            ubbi_word.append(f'ub{letter}')
        else:
            ubbi_word.append(letter)

    print(ubbi_word)

    if eng_word[0] in string.ascii_uppercase:
        ubbi_word[0] = ubbi_word[0].capitalize()
    
    return ''.join(ubbi_word)


def remove_authors_names(text, names):
    """Given a string (text) and a list of strings (names),
    remove any occurence of a name from text and return it.
    """
    output = text

    for one_name in names:
        output = output.replace(one_name, '_' * len(one_name))

    return output

def url_encode(a_string):
    """Given a string, replace any character that
        isn't a letter or number with % and its two-digit
        hex code.
    """
    valid_char = string.ascii_letters + string.digits
    output = list()
    for letter in a_string:
        if letter not in valid_char:
            to_hex = hex(ord(letter))
            to_hex = to_hex.replace('0x', '%')
            output.append(to_hex)
        else:
            output.append(letter)
    return ''.join(output)

if __name__ == "__main__":
    print(ubbi_dubbi('milk'))
    print(ubbi_dubbi('elephant')) 
    print(ubbi_dubbi('Milk'))
    print(ubbi_dubbi('Elephant')) 
    print(ubbi_dubbi_capital('Milk'))
    print(ubbi_dubbi_capital('Elephant')) 
    print(ubbi_dubbi_capital('MiLk'))
    print(ubbi_dubbi_capital('ElePhant')) 
    print(remove_authors_names('This article is written by Boldrin and Cox', ['Boldrin', 'Cox'])) 
    print(url_encode('Ci@o!?')) 




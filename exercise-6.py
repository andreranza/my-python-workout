def pig_latin(word):
    '''Translate english words to pig latin (solution)'''
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

def pl_sentence(a_sentence):
    '''Translate into pig latin more than one word'''
    input = a_sentence.split()
    output = ''.join(pig_latin(f'word{" "}') for word in input)
    return output

def nonsensical_sentence(file_path):
    nosense = list()
    with open(file_path) as f:
        for i, line in enumerate(f):
            if i < 10:
                stripped_line = line.strip()
                for j, word in enumerate(stripped_line.split()):
                    if j == i:
                        nosense.append(pig_latin(word))
            else:
                break
    output = ''.join(f'{word}{" "}' for word in nosense)
    return output.strip()

if __name__ == "__main__":
    test = 'this is a test translation'
    #print(pl_sentence(test))
    print(nonsensical_sentence('data/exercise-6-data.txt'))


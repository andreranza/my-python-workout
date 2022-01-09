def pl_sentence(a_sentence):
    '''Translate into pig latin more than one word'''
    input = a_sentence.split()
    output = ''.join(pig_latin(f'word{" "}') for word in input)
    return output

def nonsensical_sentence(file_path):
    """Given a text file, return a sentence from the nth
    word for line n, for each of the first 10 lines. 
    """
    nosense = list()
    with open(file_path) as f:
        for i, line in enumerate(f):
            if i < 10:
                stripped_line = line.strip()
                for j, word in enumerate(stripped_line.split()):
                    if j == i:
                        nosense.append(word)
            else:
                break

    output = ''.join(f'{word}{" "}' for word in nosense)
    return output.strip()

def word_per_line(filename):
    """Given a text file, return a sentence from the nth
    word for line n, for each of the first 10 lines. (solution)
    """
    output = []

    for n, one_line in enumerate(open(filename)):
        words = one_line.split()

        if not words:
            continue

        if n >= 10:
            break

        if n >= len(words):
            output.append(words[-1])
        else:
            output.append(words[n])

    return ' '.join(output)

if __name__ == "__main__":
    test = 'this is a test translation'
    print(pl_sentence(test))
    print(nonsensical_sentence('data/exercise-6-data.txt'))
    print(word_per_line('data/exercise-6-data.txt'))


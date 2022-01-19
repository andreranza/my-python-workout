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

# apache log file error example:
# 127.0.0.1 - - [28/Jul/2006:10:27:32 -0300] "GET /hidden/ HTTP/1.0" 404 7218
def find_ip_404_error(log_file_name):
    '''Find ip of a 404 error in apache log file'''
    with open(log_file_name) as lf:
        for line in lf:
            if ' 404 ' in line:
                ip = line.split()[0]
    return ip

def transpose_string(string_to_transpose):
    '''Transpose, a list of strings in which each 
        string contains multiple words separated by whitespace'''
    list_of_lists = list()
    for item in string_to_transpose:
        list_of_lists.append(item.split())

    transposed = list()
    for i in range(len(list_of_lists)):
        row = list()
        for sublist in list_of_lists:
            row.append(sublist[i])
        transposed.append(row)

    transposed_final = list()
    for sublist in transposed:
        transposed_final.append(' '.join(sublist))
    
    return transposed_final
    
if __name__ == "__main__":
    test = 'this is a test translation'
    print(pl_sentence(test))
    print(nonsensical_sentence('data/exercise-6-data.txt'))
    print(find_ip_404_error('data/apache-log-file.txt'))
    test = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    print(transpose_string(test))



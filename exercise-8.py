def strsort(a_string):
    output = sorted(a_string)
    return ''.join(output)

def strsort2(a_string):
    output = sorted(a_string.split())
    return ','.join(output)

def strsort3(txt_file_path):
    """Which is the last word, alphabetically in a text file?"""
    with open(txt_file_path, 'r') as f:
        sorted_output = sorted(f.read().split())
    return sorted_output[-1]

def strsort4(txt_file_path):
    """Which is the longest word in a text file"""
    with open(txt_file_path, 'r') as f:
        splitted_output = set(f.read().split())
    
    lenghts = list((map(len, splitted_output)))

    words_lengths = dict(zip(splitted_output, lenghts))

    # try to handle case with multiple words the same maximum lenght 
    max_lenghts = {v:k for k, v in words_lengths.items()}
    return max_lenghts[max(max_lenghts)]

    # if two words with same lenghts, only one is printed
    #return max(words_lengths, key=words_lengths.get) 
    
if __name__ == "__main__":
    print(strsort('cba'))
    print(strsort2('Tom Dick Harry'))
    print(strsort3('data/exercise-6-data.txt'))
    print(strsort4('data/exercise-6-data.txt'))

'''Create a text file to be used in exercise 6.'''

import glob
from pathlib import Path

input_path = Path(glob.glob('data/*.txt')[0])

with open(input_path) as f:
    txt_file = f.readline().strip().split()

with open('data/exercise-6-data.txt', 'w') as f:
    for i, word in enumerate(txt_file, start=1):
        if i % 10 == 0:
            f.write(word + '\n')
        else:
            f.write(word + ' ')

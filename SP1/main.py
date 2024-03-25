import os
import re

import nltk

try:
    nltk.data.find('tokenizers/punkt.zip')
except LookupError:
    nltk.download('punkt')

if __name__ == '__main__':
    input_file = []
    file = 'input/ukazka_HDS.ortho.txt'  # 'vety_HDS.ortho.txt'
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            input_file.append(line.strip().lower())
    # print(input_file)

    input_file_tokens = [nltk.word_tokenize(line) for line in input_file]
    # print(input_file_tokens)

    EPA = {'i': 'i',    # vokaly
           'e': 'e',
           'a': 'a',
           'o': 'o',
           'u': 'u',
           'í': 'I',
           'é': 'E',
           'á': 'A',
           'ó': 'O',
           'ú|ů': 'U',
           'ou': 'y',    # diftongy
           'au': 'Y',
           'eu': 'F',
           'f': 'f',    #fikativy
           'v': 'v',
           's': 's',
           'z': 'z',
           'š': 'S',
           'ž': 'Z',
           'ch': 'x',
           'h': 'h',
           'l': 'l',
           'r': 'r',
           'ř': 'r',
           'j': 'j',
           'p': 'p',      #plozivy
           'b': 'b',
           't': 't',
           'd': 'd',
           'ť': 'T', 'tě': 'Te',
           'ď': 'D', 'dě': 'De',
           'k': 'k',
           'g': 'g',
           'm': 'm',  # nazály
           'n': 'n',
           'ň': 'J', 'ně': 'Je',
           'c': 'c',  #afrikály
           'č': 'C',
           'dz': 'w',
           'dž': 'W',
           'ng': 'Ng', 'nk': 'Nk',     # významné alofony
           '\.': '$'
           }
    # Extract patterns from dictionary
    EPA_patterns = list(EPA.keys())
    # Compile dictionary patterns
    patterns = [re.compile(p) for p in EPA_patterns]
    # Replace
    # print(input_file_tokens[0])
    sentence_tokens = []
    output_file_tokens = []
    for sentence in input_file_tokens:
        for token in sentence:
            temp = token
            for p in patterns:
                temp = re.sub(pattern=p, repl=EPA[p.pattern], string=temp)
            sentence_tokens.append(temp)
        sentence_tokens.insert(0,'$')
        output_file_tokens.append(sentence_tokens.copy())
        sentence_tokens.clear()
    print(input_file_tokens)
    print(output_file_tokens)

    with open('out.txt', 'w', encoding='utf-8') as f:
        for sentence in output_file_tokens:
            line = '|'+'|'.join(sentence) + '|\n'
            f.write(line)


    # Add word dividers
    # print(r' '.join('(' + k + ')' for k in patterns.keys()))
    # print(",".join(patterns.values()))
    # reg = list(patterns.keys())[0]
    # pat = re.compile("|".join(patterns))
    # print(reg)
    # print(input_file_tokens[0])
    # print(re.sub(pattern=reg, repl=patterns[reg], string=input_file[0]))
    # print(re.sub(pattern=pat, string=input_file[0]))

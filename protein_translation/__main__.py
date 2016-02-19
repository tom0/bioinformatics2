import encoding
import protein_translation
import sys

switch = sys.argv[1]
filename = sys.argv[2]

with open(filename, 'r') as f:
    if switch == 'encoding':
        text = f.readline().strip()
        peptide = f.readline().strip()
        print('\n'.join(encoding.encode(text, peptide)))

    else:
        input = f.readline().strip()
        print(protein_translation.translate(input))

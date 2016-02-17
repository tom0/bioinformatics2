import protein_translation, sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    input = f.readline().strip()
    print(protein_translation.translate(input))

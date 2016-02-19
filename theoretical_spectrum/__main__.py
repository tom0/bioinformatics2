import sys
from theoretical_spectrum.spectrum import generate

filename = sys.argv[1]

with open(filename, 'r') as f:
    peptide = f.readline().strip()
    print(' '.join([str(x) for x in generate(peptide)]))

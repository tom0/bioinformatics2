import kmer_reconstruction, sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    kmers = [line.strip() for line in f.readlines() if line.strip() != '']
    print(kmer_reconstruction.reconstruct(kmers))

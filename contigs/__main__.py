import contigs
import kmer_reconstruction
import sys
import debruijn


filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip() != '']
    graph = debruijn.create_from_patterns(lines)
    res = contigs.maximal_non_branching_paths(graph)
    cgs = [kmer_reconstruction.reconstruct(ks) for ks in res]
    output = '\n'.join(cgs)
    print(output)

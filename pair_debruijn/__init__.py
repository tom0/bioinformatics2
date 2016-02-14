from collections import defaultdict

from overlapgraph import prefix, suffix


def create_from_patterns(kmer_pairs):
    edges = defaultdict(list)
    for kmer_pair in kmer_pairs:
        p = (prefix(kmer_pair[0]), prefix(kmer_pair[1]))
        edges[p].append((suffix(kmer_pair[0]), suffix(kmer_pair[1])))
    return edges

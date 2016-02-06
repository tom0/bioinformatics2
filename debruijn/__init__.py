from collections import defaultdict

import composition
from overlapgraph import suffix, prefix


def create_from_patterns(kmers):
    edges = defaultdict(list)
    for kmer in kmers:
        p = prefix(kmer)
        edges[p].append(suffix(kmer))

    return edges


def create(text, k):
    kmers = composition.composition(text, k)
    return create_from_patterns(kmers)


def to_string(graph):
    res = []
    for key, value in graph.items():
        res.append("{0} -> {1}".format(key, ",".join(value)))
    return "\n".join(res)

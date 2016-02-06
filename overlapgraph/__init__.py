from collections import defaultdict


def prefix(kmer):
    return kmer[:-1]


def suffix(kmer):
    return kmer[1:]


def create(kmers):
    suffixes = defaultdict(list)
    for kmer in kmers:
        s = suffix(kmer)
        suffixes[s].append(kmer)

    prefixes = defaultdict(list)
    for kmer in kmers:
        p = prefix(kmer)
        prefixes[p].append(kmer)

    edges = []
    for s in suffixes:
        if s in prefixes:
            edges += [(x, y) for x in suffixes[s] for y in prefixes[s]]

    return edges


def graph_to_string(graph):
    res = []
    for (x, y) in graph:
        res.append("{0} -> {1}".format(x, y))
    return "\n".join(res)

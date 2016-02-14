import debruijn
import eulerian.path
import kmer_reconstruction


def reconstruct(kmers):
    graph = debruijn.create_from_patterns(kmers)
    path = eulerian.path.find_path(graph)
    text = kmer_reconstruction.reconstruct(path)
    return text

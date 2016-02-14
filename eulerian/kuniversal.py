import eulerian.cycle
import kmer_reconstruction
import debruijn


def create_circular_string(k):
    format_string = '{0:0' + str(k) + 'b}'
    strings = [format_string.format(x) for x in range(0, 2 ** k)]
    graph = debruijn.create_from_patterns(strings)
    cycle = eulerian.cycle.find_cycle(graph)[:-(k-1)]

    text = kmer_reconstruction.reconstruct(cycle)
    return text

import eulerian.cycle
import eulerian.path
import eulerian.util
import eulerian.reconstruction
import sys

mode = sys.argv[1]
filename = sys.argv[2]

with open(filename, 'r') as f:
    if mode == 'path':
        edges_lines = [line.strip() for line in f.readlines() if line.strip() != '']
        graph = eulerian.util.parse_edges(edges_lines)
        result = eulerian.path.find_path(graph)
        print(eulerian.util.to_string(result))
    elif mode == 'cycle':
        edges_lines = [line.strip() for line in f.readlines() if line.strip() != '']
        graph = eulerian.util.parse_edges(edges_lines)
        result = eulerian.cycle.find_cycle(graph)
        print(eulerian.util.to_string(result))
    elif mode == 'reconstruct':
        f.readline() # Swallow k
        kmers = [line.strip() for line in f.readlines() if line.strip() != '']
        result = eulerian.reconstruction.reconstruct(kmers)
        print(result)

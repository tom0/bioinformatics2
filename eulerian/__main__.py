import eulerian.cycle
import eulerian.kuniversal
import eulerian.path
import eulerian.reconstruction
import eulerian.util
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
    elif mode == 'kuniversal':
        k = int(f.readline().strip())
        result = eulerian.kuniversal.create_circular_string(k)
        print(result)

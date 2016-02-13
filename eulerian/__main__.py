import eulerian.cycle
import eulerian.path
import eulerian.util
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    mode = f.readline()
    edges_lines = [line.strip() for line in f.readlines() if line.strip() != '']
    graph = eulerian.util.parse_edges(edges_lines)
    if mode == 'path':
        result = eulerian.path.find_path(graph)
    else:
        result = eulerian.cycle.find_cycle(graph)
    print(eulerian.util.to_string(result))

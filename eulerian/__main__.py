import eulerian.cycle, sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    edges_lines = [line.strip() for line in f.readlines() if line.strip() != '']
    graph = eulerian.cycle.parse_edges(edges_lines)
    cycle = eulerian.cycle.find_cycle(graph)
    print(eulerian.cycle.cycle_to_string(cycle))

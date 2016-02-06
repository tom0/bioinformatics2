import overlapgraph, sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    kmers = [line.strip() for line in f.readlines() if line.strip() != '']
    graph = overlapgraph.create(kmers)
    print(overlapgraph.graph_to_string(graph))

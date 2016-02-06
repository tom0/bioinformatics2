import debruijn, sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    k = int(f.readline())
    text = f.readline()
    graph = debruijn.create(text, k)
    print(debruijn.to_string(graph))

import debruijn, sys

mode = sys.argv[1]
filename = sys.argv[2]

with open(filename, 'r') as f:
    if mode == 'patterns':
        kmers = [line.strip() for line in f.readlines() if line.strip() != '']
        graph = debruijn.create_from_patterns(kmers)
    else:
        k = int(f.readline())
        text = f.readline()
        graph = debruijn.create(text, k)

    print(debruijn.to_string(graph))

import eulerian.path
import pair_debruijn
import pair_debruijn.util
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    k_d = f.readline()
    parts = k_d.split(' ')
    k = int(parts[0].strip())
    d = int(parts[1].strip())
    lines = [line.strip() for line in f.readlines() if line.strip() != '']
    gapped_patterns = pair_debruijn.util.parse_gapped_patterns(lines)
    graph = pair_debruijn.create_from_patterns(gapped_patterns)
    path = eulerian.path.find_path(graph)
    text = pair_debruijn.util.string_spelled_by_gapped_patterns(path, k, d)
    print(text)


def parse_edges(edges_lines):
    edges = {}
    for line in edges_lines:
        parts = line.split('->')
        from_node = int(parts[0].strip())
        edges[from_node] = [int(p.strip()) for p in parts[1].split(',')]
    return edges


def to_string(cyc):
    return '->'.join([str(c) for c in cyc])
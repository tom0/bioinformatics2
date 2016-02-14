def maximal_non_branching_paths(graph):
    from collections import defaultdict
    incoming_counts = defaultdict(int)
    for node, outgoings in graph.items():
        for x in outgoings:
            incoming_counts[x] += 1

    paths = []
    connected = []

    def collect_non_branching_paths(node, outgoings):
        outgoing_count = len(outgoings)
        if outgoing_count > 0:
            for outgoing in outgoings:
                u = outgoing
                nbp = [node, u]
                outgoing_count = 0
                if u in graph:
                    outgoing_count = len(graph[u])

                while incoming_counts[u] == 1 and outgoing_count == 1 and u != node:
                    nbp += graph[u]
                    u = graph[u][0]
                    outgoing_count = 0
                    if u in graph:
                        outgoing_count = len(graph[u])

                paths.append(nbp)
                connected.extend(nbp)

    for node, outgoings in graph.items():
        if not (incoming_counts[node] == 1 and len(outgoings) == 1):
            collect_non_branching_paths(node, outgoings)

    for node, outgoings in graph.items():
        if node in connected:
            continue
        collect_non_branching_paths(node, outgoings)

    return paths

def get_contigs(graph):
    paths = maximal_non_branching_paths(graph)

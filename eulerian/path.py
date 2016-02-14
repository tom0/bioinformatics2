def balance_graph(edges):
    from collections import defaultdict
    incoming_counts = defaultdict(int)
    for node, outgoings in edges.items():
        for x in outgoings:
            incoming_counts[x] += 1

    missing_nodes = filter(lambda i: i not in edges, incoming_counts)
    for node in missing_nodes:
        edges[node] = []

    destination = filter(lambda i: len(edges[i]) < incoming_counts[i], edges)[0]
    origin = filter(lambda i: len(edges[i]) > incoming_counts[i], edges)[0]

    edges[destination].append(origin)

    return edges, destination, origin


def find_path(edges):
    (edges, destination_node, origin_node) = balance_graph(edges)
    result = []
    start_node = edges.keys()[0]
    current_node = start_node

    nodes_with_unexplored_edges = set()
    while len(edges) > 0:
        result.append(current_node)
        next_node = edges[current_node][0]
        edges[current_node].remove(next_node)
        if len(edges[current_node]) == 0:
            del edges[current_node]
            if current_node in nodes_with_unexplored_edges:
                nodes_with_unexplored_edges.remove(current_node)
        else:
            nodes_with_unexplored_edges.add(current_node)

        if next_node == start_node and len(edges) > 0 and next_node not in edges:
            unexplored_node = nodes_with_unexplored_edges.pop()
            new_start_index = result.index(unexplored_node)
            result = result[new_start_index:] + result[:new_start_index]
            next_node = unexplored_node
            start_node = unexplored_node

        current_node = next_node

    # Shift the list around so that the destination is last
    end_index = result.index(destination_node)
    result = result[end_index+1:] + result[:end_index+1]

    return result

def has_common(edges, a, b):
    graph = get_graph(edges)

    a_parents = set()
    b_parents = set()

    get_parents(graph, a, a_parents)
    get_parents(graph, b, b_parents)

    for a_p in a_parents:
        if a_p in b_parents:
            return True
    return False

def get_graph(edges):
    graph = {}

    for edge in edges:
        parent, child = edge

        if child not in graph:
            graph[child] = []
        graph[child].append(parent)
        if parent not in graph:
            graph[parent] = []

    return graph

def get_parents(graph, node, parents):
    parents.add(node)

    if not graph[node]:
        return

    for parent in graph[node]:
        parents.add(parent)
        get_parents(graph, parent, parents)

edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
print(has_common(edges, 4, 5))

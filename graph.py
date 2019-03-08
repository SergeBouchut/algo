def breadth_search(graph, orig, dest):
    path = (orig,)
    if dest == orig:
        return path
    queue = [(neighbourg, path) for neighbourg in graph.get(orig, [])]
    while queue:
        candidate, path = queue.pop(0)
        if dest == candidate:
            return path + (dest,)
        queue += [(neighbourg, path + (candidate,))
                  for neighbourg in graph.get(candidate, [])]
    return None


assert breadth_search({
    'a': ['b', 'c'],
    'b': ['c'],
}, orig='a', dest='c') == ('a', 'c')
assert breadth_search({
    'a': ['b', 'c'],
    'b': ['a', 'c'],
    'c': ['d'],
}, orig='a', dest='d') == ('a', 'c', 'd')


def dijkstra(graph, orig, dest):
    costs = {n: float('inf') for n in graph.keys()}
    paths = {}

    costs[orig] = 0
    paths[orig] = (orig,)

    unprocessed_nodes = list(graph.keys())
    while unprocessed_nodes:
        # pick the unprocessed node with the lower cost
        unprocessed_nodes.sort(key=lambda node: costs[node])
        node = unprocessed_nodes.pop(0)
        
        if node == dest:
            return paths[dest]

        # recompute neighbourg cost based on edge cost
        for neighbourg, edge_cost in graph[node]:
            new_cost = edge_cost + costs[node]
            if new_cost < costs[neighbourg]:
                costs[neighbourg] = new_cost
                paths[neighbourg] = paths[node] + (neighbourg,)
    return None


assert dijkstra({
    'a': [('b', 1), ('c', 5)],
    'b': [('c', 2)],
    'c': [],
}, orig='a', dest='c') == ('a', 'b', 'c')
assert dijkstra({
    'a': [('c', 18), ('e', 3)],
    'b': [('a', 8), ('c', 4)],
    'c': [],
    'd': [('b', 1)],
    'e': [('b', 10), ('d', 2)],
}, orig='a', dest='c') == ('a', 'e', 'd', 'b', 'c')

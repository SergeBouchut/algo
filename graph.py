from collections import defaultdict


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


def a_star(orig, dest, barriers):
    neighbourgs = defaultdict(list)
    distances = {}
    costs = {}
    costs_with_distances = {}
    paths = {}

    def get_neighbourgs(node):
        if node not in neighbourgs.keys():
            x, y = node
            for neighbourg in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
                if neighbourg not in barriers:
                    neighbourgs[node].append(neighbourg)
        return neighbourgs[node]

    def get_distance(node):
        if node not in distances.keys():
            x, y = node
            X, Y = dest
            distances[node] = abs(X - x) + abs(Y - y)
        return distances[node]

    costs[orig] = 0
    costs_with_distances[orig] = get_distance(orig)
    paths[orig] = (orig,)

    processed_nodes = []
    unprocessed_nodes = [orig]
    while unprocessed_nodes:
        # pick the unprocessed node with the lower cost
        unprocessed_nodes.sort(key=lambda node: costs_with_distances.get(node, float('inf')))
        node = unprocessed_nodes.pop(0)
        processed_nodes.append(node)

        if node == dest:
            return paths[dest]

        # recompute neighbourg cost based on edge cost
        for neighbourg in get_neighbourgs(node):
            if (
                neighbourg not in unprocessed_nodes
                and neighbourg not in processed_nodes
            ):
                unprocessed_nodes.append(neighbourg)

            new_cost = 1 + costs[node]
            if new_cost < costs.get(neighbourg, float('inf')):
                costs[neighbourg] = new_cost
                costs_with_distances[neighbourg] = new_cost + get_distance(neighbourg)
                paths[neighbourg] = paths[node] + (neighbourg,)
    return None


assert a_star((0, 0), (0, 3), []) == ((0, 0), (0, 1), (0, 2), (0, 3))
assert a_star((0, 0), (0, -3), []) == ((0, 0), (0, -1), (0, -2), (0, -3))
assert a_star((0, 0), (1, 3), []) == ((0, 0), (0, 1), (0, 2), (0, 3), (1, 3))
# with barrier
assert a_star((0, 0), (0, 3), [(0, 2)]) == ((0, 0), (0, 1), (-1, 1), (-1, 2), (-1, 3), (0, 3))
assert a_star((0, 0), (1, 3), [(0, 2)]) == ((0, 0), (0, 1), (1, 1), (1, 2), (1, 3))

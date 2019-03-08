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

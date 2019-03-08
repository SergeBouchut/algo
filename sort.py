def quick_sort(items):
    if len(items) < 2:
        return items
    pivot = items[0]
    left, right = [], []
    for item in items[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


assert quick_sort([]) == []
assert quick_sort([42]) == [42]
assert quick_sort([21, 42]) == [21, 42]
assert quick_sort([42, 21]) == [21, 42]
assert quick_sort([-30, 21, 42]) == [-30, 21, 42]
assert quick_sort([21, -30, 42]) == [-30, 21, 42]
assert quick_sort([42, -30, 21]) == [-30, 21, 42]

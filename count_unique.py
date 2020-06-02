from collections import Counter


def count_unique(lst: list):
    return dict(Counter(lst))


print(count_unique([1,2,2,3,3,3,4,4,4,5]))








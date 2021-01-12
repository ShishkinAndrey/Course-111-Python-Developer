from typing import List
import random

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) < 2:
        return container
    else:
        point = container[0]
        less = [i for i in container[1:] if i <= point]
        bigger = [i for i in container[1:] if i > point]
    return sort(less) + [point] + sort(bigger)

if __name__ == '__main__':
    arr = [random.randint(0, 100) for _ in range(10)]
    print(sort(arr))
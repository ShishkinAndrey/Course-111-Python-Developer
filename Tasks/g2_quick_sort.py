from typing import List
import random

# 1 вариант
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
        left_container = [i for i in container[1:] if i < point]
        middle_container = [i for i in container if i == point]
        right_container = [i for i in container[1:] if i > point]
    return sort(left_container) + middle_container + sort(right_container)

# 2 cпособ с использованием счетчика
def sort_(container: List[int]) -> List[int]:
    def sort__(container, start, end):
        if start >= end:
            return None
        i = start
        j = end
        point = container[(start + end) // 2]
        while i <= j:
            while container[i] < point:
                i += 1
            while container[j] > point:
                j -= 1
            if i <= j:
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1
        sort__(container, start, i-1)
        sort__(container, i, end)
        return container
    return sort__(container,0,len(container)-1)

if __name__ == '__main__':
    arr = [random.randint(-100, 100) for _ in range(30)]
    print(sort_(arr))

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


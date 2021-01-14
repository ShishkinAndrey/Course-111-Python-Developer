from typing import List
import random

# 1 вариант
# def sort(container: List[int]) -> List[int]:
#     """
#     Sort input container with quick sort
#
#     :param container: container of elements to be sorted
#     :return: container sorted in ascending order
#     """
#     if len(container) < 2:
#         return container
#     else:
#         point = container[0]
#         left_container = [i for i in container[1:] if i < point]
#         middle_container = [i for i in container if i == point]
#         right_container = [i for i in container[1:] if i > point]
#     return sort(left_container) + middle_container + sort(right_container)

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <2:
        return container
    else:
        point = len(container) // 2
        i = 0
        j = -1
        while i < j:
            while container[i] < point:
                i += 1
            while container[j] > point:
                j -= 1
            container[i], container[j] = container[j], container[i]
            if i >= j:
                break
        sort(container[:j])

if __name__ == '__main__':
    arr = [2,10,3,14,7,45,5]
    print(sort(arr))

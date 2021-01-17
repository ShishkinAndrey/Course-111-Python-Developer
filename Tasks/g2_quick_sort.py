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

def sort_(container, start, end):
    if start >= end:
        return container
    i = start
    j = end
    point = container[len(container) // 2]

    while i <= j:
        while container[i] < point:
            i += 1
        while container[j] > point:
            j -= 1
        if i <= j:
            container[i], container[j] = container[j], container[i]
            i += 1
            j -= 1
            return sort_(container, i, j)
            # sort_(container[j:], j, end)

if __name__ == '__main__':
    arr = [2,10,3,14,7]
    print(sort_(arr,0,len(arr)-1))
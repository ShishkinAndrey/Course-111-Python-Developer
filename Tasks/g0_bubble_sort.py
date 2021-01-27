from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    correct_compare = True
    while correct_compare:
        correct_compare = False
        for i in range(len(container)-1):
            if container[i] > container[i + 1]:
                container[i], container[i+1] = container[i+1], container[i]
                correct_compare = True
    return container

if __name__ == '__main__':
    lst = [14, 3, 17, 12,1,22,5]
    print(sort(lst))

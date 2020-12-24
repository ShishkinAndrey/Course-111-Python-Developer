from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if not arr:
        return None
    left = 0
    right = len(arr) - 1
    current_index = (left + right) // 2
    while True:
        if elem < arr[current_index]:
            right = current_index - 1
        elif elem > arr[current_index]:
            left = current_index + 1
        else:
            while arr[current_index-1] == elem:
                current_index -= 1
            return current_index
        current_index = (left + right) // 2
        if left > right:
            return None


if __name__ == '__main__':
    print(binary_search(2, [1, 2, 2, 2, 2, 2]))
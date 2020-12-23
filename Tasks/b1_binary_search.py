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
    left_border = 0
    right_border = len(arr) - 1
    current_index = 0
    i = 0
    print(arr)
    while True:
        if left_border > right_border:
            return None
        if arr[left_border] == elem:

            return left_border
        if arr[right_border] == elem:
            while arr[right_border-1] == elem:
                right_border -= 1
            return right_border
        current_index = (left_border + right_border) // 2
        print(f'{i}: current index - {current_index} ')
        print(f'{i}: left - {left_border} ')
        print(f'{i}: right - {right_border} ')
        if elem == arr[current_index]:
            return arr.index(elem)
        elif elem < arr[current_index]:
            right_border = current_index - 1
        elif elem > arr[current_index]:
            left_border = current_index + 1
        i += 1




if __name__ == '__main__':
    print(binary_search(2, [1, 2, 2, 2]))
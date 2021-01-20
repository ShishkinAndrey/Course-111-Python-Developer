from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    current_index = len(arr) // 2
    if not arr:
        return None
    elif len(arr) == 1:
        return current_index if arr[current_index] == elem else None
    elif arr[current_index] == elem:
        while arr[current_index - 1] == elem:
            current_index -= 1
        return current_index
    else:
        if elem < arr[current_index]:
            return binary_search(elem, arr[:current_index])
        elif elem > arr[current_index]:
            right_binary = binary_search(elem, (arr[current_index:]))
            return current_index + right_binary if right_binary is not None else None


if __name__ == '__main__':
    print(binary_search(2, [1, 2, 2, 2]))
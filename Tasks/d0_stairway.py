from typing import Union, Sequence


def stairway_path__(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    '''прямой метод'''
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    list_value = [i == 0 for i in range(len(stairway))]
    list_value[0] = stairway[0]
    list_value[1] = stairway[1]
    for i in range(2, len(stairway)):
        list_value[i] = stairway[i] + min(list_value[i-1], list_value[i-2])
    print(list_value)
    return list_value[-1]

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]: #обратный
    '''обратный метод'''
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    list_value = [float('inf') for i in range(len(stairway))]
    list_value[0] = stairway[0]
    print(stairway)
    for i in range(1, len(stairway)-1):
        value = list_value[i]  #беск
        new_value = stairway[i] + list_value[i-1]
        list_value[i] = min(value, new_value)
        try:
            value = list_value[i + 1]
            new_value = stairway[i + 1] + list_value[i-1]
            list_value[i + 1] = min(value, new_value)
        except IndexError:
            pass
    print(list_value)
    return list_value[-2]


def stairway_path_(stairway: Sequence[Union[float, int]]) -> Union[float, int]: # рекурсивный
    '''ленивый метод'''
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    list_value = [i == 0 for i in range(len(stairway))]
    list_value[0] = stairway[0]
    list_value[1] = stairway[1]

    def calc_value(i):
        if list_value[i] != 0:
            return list_value[i]
        list_value[i] = stairway[i] + min(calc_value(i - 1), calc_value(i - 2))
    for i in range(2, len(stairway)):
        calc_value(i)
    return list_value[-1]



    



if __name__ == '__main__':
    lst = [4, 1, 3, 2, 3, 4]
    print(stairway_path(lst))
    # print(stairway_path_(lst))
    print(stairway_path__(lst))
from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    '''прямой метод'''
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    list_value = [i==0 for i in range(len(stairway))]
    list_value[0] = stairway[0]
    list_value[1] = stairway[1]
    for i in range(2, len(stairway)):
        list_value[i] = stairway[i] + min(list_value[i-1], list_value[i-2])
    return list_value[-1]

def stairway_path_(stairway: Sequence[Union[float, int]]) -> Union[float, int]: #обратный
    '''обратный метод'''
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    ''' ДОДЕЛАТЬ'''

def stairway_path__(stairway: Sequence[Union[float, int]]) -> Union[float, int]: # рекурсивный
    '''ленивый метод'''
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    memory_dict = {}
    memory_dict[0] == stairway[0]
    



if __name__ == '__main__':
    print(stairway_path([4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2]))
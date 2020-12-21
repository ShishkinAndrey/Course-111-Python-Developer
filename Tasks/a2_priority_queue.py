"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
items_list = []
queue_priority = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    items_list.insert(0, (elem, priority))
    items_list.sort(key=lambda x: x[1], reverse=True)
    queue_priority.clear()
    for i in items_list:
        queue_priority.append(i[0])
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    items_list.pop(-1)
    return None if len(queue_priority) == 0 else queue_priority.pop(-1)


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return None if ind >= len(queue_priority) else queue_priority[-1-ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    queue_priority.clear()
    return None

if __name__ == '__main__':
    enqueue(10, 0)
    enqueue(0, 10)

    print(queue_priority)
    print(items_list)
    dequeue()
    print('-'*10)
    print(items_list)
    print(queue_priority)
    enqueue(1, 10)
    enqueue(6, 5)
    print('-' * 10)
    print(items_list)
    print(queue_priority)
    dequeue()
    print(items_list)
    print(queue_priority)


    #
    # enqueue(5, 5)



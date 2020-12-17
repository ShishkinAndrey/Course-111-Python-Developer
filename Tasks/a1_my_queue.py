"""
My little Queue
"""
from typing import Any

my_queue = [] #слева конец очереди, справа начало

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    # print(elem)
    my_queue.insert(0, elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if not my_queue:
        return None
    else:
        return my_queue.pop()


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    # print(ind)
    if ind <= len(my_queue):
        return my_queue[-1-ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_queue.clear()
    return None

if __name__ == '__main__':
    print(my_queue)
    enqueue(3)
    print(my_queue)
    enqueue(5)
    print(my_queue)
    enqueue(35)
    print(my_queue)
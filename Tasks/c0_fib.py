def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n <0:
        raise ValueError()
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n-2) + fib_recursive(n-1)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)
    return 0

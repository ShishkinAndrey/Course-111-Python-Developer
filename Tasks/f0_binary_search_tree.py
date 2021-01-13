"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
import networkx as nx
bst = {}

def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
#     def _insert(bin_tree: dict):
#         if not bin_tree:
#             bin_tree = {
#                 'key' == key,
#                 'value' == value,
#                 'left' == {},
#                 'right' == {}
#             }
#         else:
#             new_bin_tree = bin_tree['left'] if key <= bin_tree['key'] else bin_tree['right']
#             _insert(new_bin_tree)
#     _insert(bst)

    def insert_(tree):
        if tree is None:
            tree = {'key': key, 'left': {}, 'right': {}}
        elif key <= tree['key']:
            btree= tree['left']
        else:
            btree = tree['right']
        insert_(btree)

    insert_(bst)

def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    print(key)
    return None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    print(key)
    return None


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    return None

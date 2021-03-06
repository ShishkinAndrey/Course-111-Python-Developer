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
    def _insert(root: dict, node: int):
        # Сравнивает ключи и вставляет node
        if not root:
            root['key'] = node
            root['value'] = value
        elif node < root['key']:
            if 'left' not in root.keys():
                root['left'] = {}
                root['left']['key'] = node
                root['left']['value'] = value
            else:
                _insert(root['left'], node)
        else:
            if 'right' not in root.keys():
                root['right'] = {}
                root['right']['key'] = node
                root['right']['value'] = value
            else:
                _insert(root['right'], node)
    _insert(bst, key)

def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    def _delete(root: dict, target: int):
        # Сравнивает ключи,находим target и удаляем
        if not root:
            return None
        if target == root['key']:
            removed_key = root.pop('key')
            removed_value = root.pop('value')
            if 'left' in root.keys():
                   root.update(root.pop('left'))
            elif 'right' in root.keys():
                   root.update(root.pop('right'))
            return (removed_key, removed_value)
        elif root['key'] < target:
            if 'right' in root.keys():
                return _delete(root['right'], target)
            else:
                raise KeyError("Do not forget about deleting non-existing keys. "
                "I think that deleting of non-existing keys should be silent, unlike search.")
        elif root['key'] > target:
            if 'left' in root.keys():
                return _delete(root['left'], target)
            else:
                raise KeyError("Do not forget about deleting non-existing keys. "
                "I think that deleting of non-existing keys should be silent, unlike search.")
    return _delete(bst, key)


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    def _find(root: dict, target:int):
        # Сравнивает ключи и находим target
        if target == root['key']:
            return root['value']
        elif root['key'] < target:
            if 'right' in root.keys():
                return _find(root['right'],target)
            else:
                raise KeyError('Search of non-existing key should be erroneous.')
        elif root['key'] > target:
            if 'left' in root.keys():
                return _find(root['left'],target)
            else:
                raise KeyError('Search of non-existing key should be erroneous.')
    return _find(bst, key)


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    bst.clear()
    return None

if __name__ == '__main__':
    insert(1,2)
    insert(0, 12)
    insert(2, 323)
    insert(-1, 324)
    insert(3, 325)
    print(bst)
    # print(find(11))
    print(remove(1))
    # print(remove(42))
    # clear()

    print(bst)
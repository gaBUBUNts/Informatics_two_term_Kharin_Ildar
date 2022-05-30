def add(tree: tuple or None, value: int) -> tuple:
    if tree is None:
        return tuple((value, None, None))
    if value < tree[0]:
        return tuple((tree[0], add(tree[1], value), tree[2]))
    if value > tree[0]:
        return tuple((tree[0], tree[1], add(tree[2], value)))


def contains(tree: tuple or None, value: int) -> bool:
    if tree is None:
        return False
    if value < tree[0]:
        return contains(tree[1], value)
    if value > tree[0]:
        return contains(tree[2], value)
    return True


def tree_lenght(tree: tuple or None) -> int:
    if tree is None:
        return 0
    else:
        return 1 + max(tree_lenght(tree[1]), tree_lenght(tree[2]))


class VersionedTree:
    def __init__(self):
        self.__versions = [None]

    def add(self, value: int) -> None:
        self.__versions.append(add(self.__versions[-1], value))

    def contains(self, version: int, value: int) -> bool:
        return contains(self.__versions[version], value)

    def height(self, version: int) -> int:
        return tree_lenght(self.__versions[version])

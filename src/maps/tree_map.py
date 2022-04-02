"""
Модуль для создания дерева двоичного поиска.

Классы:
    Knot: Класс для создания узлов дерева двоичного поиска.

    TreeMap: Класс для создания дерева двоичного поиска.
"""


from src.maps.base_map import BaseMap


class Knot:
    """
    Класс для создания узлов дерева двоичного поиска.

    Атрибуты:
        key: ключ узла.

        data: данные, хранящиеся в узле.

        right: ссылка на узел, являющийся правым потомком узла в дереве двоичного поиска.

        left: ссылка на узел, являющийся левым потомком узла в дереве двоичного поиска.
    """

    def __init__(self, key, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left
        self.key = key

    def __eq__(self, other):
        if isinstance(other, Knot):
            if self.key == other.key:
                return True
            return False
        return False

    def __ne__(self, other):
        if isinstance(other, Knot):
            if self == other:
                return False
            return True
        return True

    def __lt__(self, other):
        if isinstance(other, Knot):
            if self.key < other.key:
                return True
            return False
        raise TypeError

    def __gt__(self, other):
        if isinstance(other, Knot):
            if self.key > other.key:
                return True
            return False
        raise TypeError


class TreeMap(BaseMap):
    """
    Класс для создания дерева двоичного поиска.

    Атрибуты:
        root: корневой узел дерева.

    Методы:
        __setitem__: вставить узел в дерево.

        __getitem__: вернуть узел дерева по ключу.

        __delitem__: удалить узел дерева по ключу.
    """

    def __init__(self, root=None):
        self.root = root
        self.length = 0

    def __setitem__(self, key, data):
        def inner_setitem(knot):
            if knot is None:
                return Knot(key, data)
            if key == knot.key:
                knot.data = data
            elif key < knot.key:
                knot.left = inner_setitem(knot.left)
            else:
                knot.right = inner_setitem(knot.right)

            return knot

        self.root = inner_setitem(self.root)
        self.length += 1

    def __getitem__(self, key):
        def inner_getitem(knot):
            if knot is None:
                raise KeyError("Элемента с таким ключем нет.")
            if key == knot.key:
                return knot
            if key > knot.key:
                return inner_getitem(knot.right)
            return inner_getitem(knot.left)

        return inner_getitem(self.root).data

    @staticmethod
    def find_min_node(knot):
        """
        Найди узел с наименьшим ключем в дереве.

        :param Knot knot: узел, который будет считаться корнем дерева.
        :return: узел с наименьшим ключем в дереве.
        """
        if knot.left is not None:
            return TreeMap.find_min_node(knot.left)
        return knot

    def __delitem__(self, key):
        def inner_delitem(knot, key):
            if knot is None:
                raise KeyError("Элемента с таким ключем нет.")
            # рекурсивно ищем узел который нужно удалить
            if key < knot.key:
                knot.left = inner_delitem(knot.left, key)
                return knot
            if key > knot.key:
                knot.right = inner_delitem(knot.right, key)
                return knot
            # Нет потомков.
            if knot.left is None and knot.right is None:
                return None
            # Есть только левый потомок.
            if knot.left is not None and knot.right is None:
                return knot.left
            # Есть только правый потомок.
            if knot.left is None and knot.right is not None:
                return knot.right
            # Есть оба потомка.
            if knot.left is not None and knot.right is not None:
                min_node = TreeMap.find_min_node(knot.right)
                knot.key = min_node.key
                knot.data = min_node.data
                knot.right = inner_delitem(knot.right, min_node.key)
                return knot
            raise KeyError

        self.root = inner_delitem(self.root, key)
        self.length -= 1

    def __iter__(self):
        def iter_node(node):
            if node is not None:
                yield from iter_node(node.left)
                yield node.key, node.data
                yield from iter_node(node.right)

        yield from iter_node(self.root)

    def __len__(self):
        return self.length


if __name__ == "__main__":
    tree = TreeMap()
    tree[6] = "kekw"
    tree[3] = "waba"
    tree[5] = "yolo"
    tree[2] = "ratat"
    tree[8] = "elims"
    tree[10] = "popoya"
    tree[7] = "gogol"
    for i in tree:
        print(i)

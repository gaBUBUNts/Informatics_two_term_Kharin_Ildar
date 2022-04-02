"""
Модуль для тестирования HashMap и TreeMap.

Классы:
    SetGetDelCase: Класс для тестирования функций set, get, del в HashMap и TreeMap.

    HashMapTests: Класс для тестирования увеличения объема HashMap.
"""


import unittest
from src.maps.hash_map import HashMap
from src.maps.tree_map import TreeMap


class SetGetDelCase(unittest.TestCase):
    """
    Класс для тестирования функций set, get, del в HashMap и TreeMap.

    Атрибуты:
        hash_map: экземпляр класса HashMap.

        tree_map: экземпляр класса TreeMap.

        one_small_tree_map: экземпляр класса TreeMap.

        two_small_tree_map: экземпляр класса TreeMap.
    Методы:
        test_set_get_item: Тест функций set и get в HashMap и TreeMap.

        test_del_item: Тест функции del в HashMap и TreeMap.
    """
    def setUp(self) -> None:
        self.hash_map = HashMap(10)
        self.tree_map = TreeMap()
        self.one_small_tree_map = TreeMap()
        self.two_small_tree_map = TreeMap()

    def test_set_get_item(self):
        """Тест функций set и get в HashMap и TreeMap."""
        # Создание экземпляра HashMap.
        for i in range(5):
            self.hash_map[i*10] = i*10+5
            self.hash_map[i] = i
        # Проверка функции set в HashMap.
        self.assertEqual(self.hash_map[1], 1)
        self.assertEqual(self.hash_map[10], 15)
        self.assertEqual(self.hash_map[30], 35)
        self.assertEqual(self.hash_map[0], 0)
        self.assertEqual(self.hash_map.inner_list[0].length, 5)
        # Попытка получить из HashMap несуществующий элемент.
        with self.assertRaises(KeyError):
            print(self.hash_map[100])
        # Создание экземпляра TreeMap.
        self.tree_map[8] = "8"
        self.tree_map[3] = "3"
        self.tree_map[12] = "12"
        self.tree_map[1] = "1"
        self.tree_map[6] = "6"
        # Проверка функции set в HashMap.
        self.assertEqual(self.tree_map[8], "8")
        self.assertEqual(self.tree_map[1], "1")
        self.assertEqual(self.tree_map[6], "6")
        # Попытка получить из дерева несуществующий узел.
        with self.assertRaises(KeyError):
            print(self.tree_map[100])

    def test_del_item_hash_map(self):
        """Тест функции del в HashMap."""
        for i in range(5):
            self.hash_map[i * 10] = i * 10
            self.hash_map[i] = i
        self.assertEqual(self.hash_map.cnt, 5)
        del self.hash_map[4]
        del self.hash_map[30]
        self.assertEqual(self.hash_map.cnt, 4)
        with self.assertRaises(KeyError):
            print(self.hash_map[4])
        with self.assertRaises(KeyError):
            print(self.hash_map[30])

    def test_del_root_tree_map(self):
        """Тест функции del в TreeMap."""
        self.tree_map[8] = "8"
        self.tree_map[3] = "3"
        self.tree_map[12] = "12"
        self.tree_map[1] = "1"
        self.tree_map[6] = "6"
        self.tree_map[0] = "0"
        self.tree_map[2] = "2"
        self.tree_map[4] = "4"
        self.tree_map[7] = "7"
        self.tree_map[5] = "5"
        self.tree_map[10] = "10"
        self.tree_map[14] = "14"
        self.tree_map[11] = "11"

        # Удаление корня во всех возможных вариациях.
        del self.tree_map[8]
        self.assertEqual(self.tree_map.root.key, 10)
        self.assertEqual(self.tree_map.root.right.key, 12)
        self.assertEqual(self.tree_map.root.left.key, 3)
        self.assertEqual(self.tree_map.root.right.left.key, 11)
        del self.tree_map[10]
        self.assertEqual(self.tree_map.root.key, 11)
        self.assertEqual(self.tree_map.root.right.key, 12)
        self.assertEqual(self.tree_map.root.left.key, 3)
        self.assertEqual(self.tree_map.root.right.left, None)
        del self.tree_map[11]
        self.assertEqual(self.tree_map.root.key, 12)
        self.assertEqual(self.tree_map.root.right.key, 14)
        self.assertEqual(self.tree_map.root.left.key, 3)
        self.assertEqual(self.tree_map.root.right.left, None)
        del self.tree_map[12]
        self.assertEqual(self.tree_map.root.key, 14)
        self.assertEqual(self.tree_map.root.right, None)
        self.assertEqual(self.tree_map.root.left.key, 3)

        self.one_small_tree_map[14] = "14"
        self.one_small_tree_map[15] = "15"

        del self.one_small_tree_map[14]
        self.assertEqual(self.one_small_tree_map.root.key, 15)
        del self.one_small_tree_map[15]
        self.assertEqual(self.one_small_tree_map.root, None)

        self.two_small_tree_map[14] = "14"
        self.two_small_tree_map[13] = "13"

        del self.two_small_tree_map[14]
        self.assertEqual(self.two_small_tree_map.root.key, 13)

    def test_del_item_tree_map(self):
        """Тест функции del в TreeMap."""
        # Удаление произвольного узла дерева (не головы)
        # во всех возможных вариациях.
        del self.tree_map[3]
        self.assertEqual(self.tree_map.root.left.key, 4)
        self.assertEqual(self.tree_map.root.left.right.key, 6)
        self.assertEqual(self.tree_map.root.left.left.key, 1)
        self.assertEqual(self.tree_map.root.left.right.left.key, 5)
        del self.tree_map[4]
        self.assertEqual(self.tree_map.root.left.key, 5)
        self.assertEqual(self.tree_map.root.left.right.key, 6)
        self.assertEqual(self.tree_map.root.left.left.key, 1)
        self.assertEqual(self.tree_map.root.left.right.left, None)
        del self.tree_map[5]
        self.assertEqual(self.tree_map.root.left.key, 6)
        self.assertEqual(self.tree_map.root.left.right.key, 7)
        self.assertEqual(self.tree_map.root.left.left.key, 1)
        self.assertEqual(self.tree_map.root.left.right.left, None)
        del self.tree_map[2]
        self.assertEqual(self.tree_map.root.left.left.right, None)
        del self.tree_map[1]
        self.assertEqual(self.tree_map.root.left.left.key, 0)
        del self.tree_map[0]
        del self.tree_map[6]
        self.assertEqual(self.tree_map.root.left.key, 7)

        # Попытка удаления несуществующего узла дерева.
        with self.assertRaises(KeyError):
            del self.tree_map[100]


class HashMapTests(unittest.TestCase):
    """
    Класс для тестирования особых функций HashMap.

    Атрибуты:
        hashmap: экземпляр класса HashMap.

    Методы:
        test_increase: тест увеличения вместимости hashmap при добавлении элементов.
    """

    def setUp(self) -> None:
        self.hashmap = HashMap(10)
        for i in range(5):
            self.hashmap[i*10] = i*10
            self.hashmap[i] = i
        # self.solution = "0\t0\n1\t1\n2\t2\n3\t3\n4\t4\nNone\nNone\nNone\nNone\nNone\n"

    def test_increase(self):
        """Тест увеличения вместимости hashmap при добавлении элементов."""
        for i in range(5, 8):
            self.hashmap[i*10] = i*10
            self.hashmap[i] = i
        self.assertEqual(self.hashmap.cnt, 9)
        self.assertEqual(self.hashmap.get_size(), 20)
        self.assertEqual(self.hashmap.inner_list[0].length, 4)


if __name__ == '__main__':
    unittest.main()

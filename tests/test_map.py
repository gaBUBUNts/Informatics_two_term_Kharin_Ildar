import unittest
from src.hash_map import *
from src.tree_map import *


class SetGetCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hash_map = HashMap(10)
        self.tree_map = TreeMap()
        self.one_small_tree_map = TreeMap()
        self.two_small_tree_map = TreeMap()

    def test_set_get_item(self):
        for i in range(5):
            self.hash_map[i*10] = i*10+5
            self.hash_map[i] = i

        self.assertEqual(self.hash_map[1], 1)
        self.assertEqual(self.hash_map[10], 15)
        self.assertEqual(self.hash_map[30], 35)
        self.assertEqual(self.hash_map[0], 0)
        self.assertEqual(self.hash_map._inner_list[0].length, 5)
        # Попытка получить из HashMap несуществующий элемент.
        with self.assertRaises(KeyError):
            print(self.hash_map[100])

        self.tree_map[8] = "8"
        self.assertEqual(self.tree_map[8], "8")
        self.tree_map[3] = "3"
        self.tree_map[12] = "12"
        self.tree_map[1] = "1"
        self.tree_map[6] = "6"
        self.assertEqual(self.tree_map[1], "1")
        self.assertEqual(self.tree_map[6], "6")
        # Попытка получить из дерева несуществующий узел.
        with self.assertRaises(KeyError):
            print(self.tree_map[100])

    def test_del_item(self):
        for i in range(5):
            self.hash_map[i * 10] = i * 10
            self.hash_map[i] = i
        self.assertEqual(self.hash_map._cnt, 5)
        del self.hash_map[4]
        del self.hash_map[30]
        self.assertEqual(self.hash_map._cnt, 4)
        with self.assertRaises(KeyError):
            print(self.hash_map[4])
        with self.assertRaises(KeyError):
            print(self.hash_map[30])

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

        # Удаление головы во всех возможных вариациях.
        del self.tree_map[8]
        self.assertEqual(self.tree_map.head.key, 10)
        self.assertEqual(self.tree_map.head.right.key, 12)
        self.assertEqual(self.tree_map.head.left.key, 3)
        self.assertEqual(self.tree_map.head.right.parent.key, 10)
        self.assertEqual(self.tree_map.head.left.parent.key, 10)
        self.assertEqual(self.tree_map.head.right.left.key, 11)
        self.assertEqual(self.tree_map.head.right.left.parent.key, 12)
        self.assertEqual(self.tree_map.head.parent, None)
        del self.tree_map[10]
        self.assertEqual(self.tree_map.head.key, 11)
        self.assertEqual(self.tree_map.head.right.key, 12)
        self.assertEqual(self.tree_map.head.left.key, 3)
        self.assertEqual(self.tree_map.head.right.parent.key, 11)
        self.assertEqual(self.tree_map.head.left.parent.key, 11)
        self.assertEqual(self.tree_map.head.right.left, None)
        self.assertEqual(self.tree_map.head.parent, None)
        del self.tree_map[11]
        self.assertEqual(self.tree_map.head.key, 12)
        self.assertEqual(self.tree_map.head.right.key, 14)
        self.assertEqual(self.tree_map.head.left.key, 3)
        self.assertEqual(self.tree_map.head.right.parent.key, 12)
        self.assertEqual(self.tree_map.head.left.parent.key, 12)
        self.assertEqual(self.tree_map.head.right.left, None)
        self.assertEqual(self.tree_map.head.parent, None)
        del self.tree_map[12]
        self.assertEqual(self.tree_map.head.key, 14)
        self.assertEqual(self.tree_map.head.right, None)
        self.assertEqual(self.tree_map.head.left.key, 3)
        self.assertEqual(self.tree_map.head.left.parent.key, 14)
        self.assertEqual(self.tree_map.head.parent, None)

        self.one_small_tree_map[14] = "14"
        self.one_small_tree_map[15] = "15"

        del self.one_small_tree_map[14]
        self.assertEqual(self.one_small_tree_map.head.key, 15)
        self.assertEqual(self.one_small_tree_map.head.parent, None)
        del self.one_small_tree_map[15]
        self.assertEqual(self.one_small_tree_map.head, None)

        self.two_small_tree_map[14] = "14"
        self.two_small_tree_map[13] = "13"

        del self.two_small_tree_map[14]
        self.assertEqual(self.two_small_tree_map.head.key, 13)
        self.assertEqual(self.two_small_tree_map.head.parent, None)

        # Удаление произвольного узла дерева (не головы)
        # во всех возможных вариациях.
        del self.tree_map[3]
        self.assertEqual(self.tree_map.head.left.key, 4)
        self.assertEqual(self.tree_map.head.left.right.key, 6)
        self.assertEqual(self.tree_map.head.left.left.key, 1)
        self.assertEqual(self.tree_map.head.left.right.parent.key, 4)
        self.assertEqual(self.tree_map.head.left.left.parent.key, 4)
        self.assertEqual(self.tree_map.head.left.right.left.key, 5)
        self.assertEqual(self.tree_map.head.left.right.left.parent.key, 6)
        self.assertEqual(self.tree_map.head.left.parent.key, 14)
        del self.tree_map[4]
        self.assertEqual(self.tree_map.head.left.key, 5)
        self.assertEqual(self.tree_map.head.left.right.key, 6)
        self.assertEqual(self.tree_map.head.left.left.key, 1)
        self.assertEqual(self.tree_map.head.left.right.parent.key, 5)
        self.assertEqual(self.tree_map.head.left.left.parent.key, 5)
        self.assertEqual(self.tree_map.head.left.right.left, None)
        self.assertEqual(self.tree_map.head.left.parent.key, 14)
        del self.tree_map[5]
        self.assertEqual(self.tree_map.head.left.key, 6)
        self.assertEqual(self.tree_map.head.left.right.key, 7)
        self.assertEqual(self.tree_map.head.left.left.key, 1)
        self.assertEqual(self.tree_map.head.left.right.parent.key, 6)
        self.assertEqual(self.tree_map.head.left.left.parent.key, 6)
        self.assertEqual(self.tree_map.head.left.right.left, None)
        self.assertEqual(self.tree_map.head.left.parent.key, 14)
        del self.tree_map[2]
        self.assertEqual(self.tree_map.head.left.left.right, None)
        del self.tree_map[1]
        self.assertEqual(self.tree_map.head.left.left.key, 0)
        self.assertEqual(self.tree_map.head.left.left.parent.key, 6)
        del self.tree_map[0]
        del self.tree_map[6]
        self.assertEqual(self.tree_map.head.left.key, 7)
        self.assertEqual(self.tree_map.head.left.parent.key, 14)

        # Попытка удаления несуществующего узла дерева.
        with self.assertRaises(KeyError):
            del self.tree_map[100]


class HashMapTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hashmap = HashMap(10)
        for i in range(5):
            self.hashmap[i*10] = i*10
            self.hashmap[i] = i
        # self.solution = "0\t0\n1\t1\n2\t2\n3\t3\n4\t4\nNone\nNone\nNone\nNone\nNone\n"

    def test_increase(self):
        for i in range(5, 8):
            self.hashmap[i*10] = i*10
            self.hashmap[i] = i
        self.assertEqual(self.hashmap._cnt, 9)
        self.assertEqual(self.hashmap.get_size(), 20)
        self.assertEqual(self.hashmap._inner_list[0].length, 4)

    # def test_to_string(self):
    #     result = self.hashmap.to_string()
    #     self.assertEqual(result, self.solution)

    # def test_from_string(self):
    #     new_hashmap = HashMap.from_string(self.solution)
    #     for i in range(5):
    #         self.assertEqual(new_hashmap[i], str(i))


if __name__ == '__main__':
    unittest.main()

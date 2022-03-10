import unittest
from src.hash_map import HashMap, List, Node


class SetGetCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hash_map = HashMap(10)

    def test_set_get_item(self):
        self.hash_map[1] = 42
        self.assertEqual(self.hash_map[1], 42)

    def test_del_item(self):
        self.hash_map[5] = 30
        del self.hash_map[5]
        self.assertEqual(self.hash_map[5], None)


if __name__ == '__main__':
    unittest.main()

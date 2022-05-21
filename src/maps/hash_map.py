"""
Модуль для создания Hash map.

Классы:
    Node:

    HashMap:
"""

from src.maps.base_map import BaseMap


class Node:
    """
    Класс для создания узлов List.

    Атрибуты:
        data: данные хранящиеся в узле.

        next: ссылка на следующий узел.
    Функции:
        compare_data: сравнить данные хранящиеся в узле с переданным значением.
    """

    def __init__(self, data=None, next_node=None):
        self._data = data
        self.next = next_node

    @property
    def data(self):
        """
        Вернуть у экземпляра Node атрибут data.

        :return: данные, хранящиеся в узле.
        """
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def compare_data(self, value) -> bool:
        """
        Сравнить данные хранящиеся в узле с переданным значением.

        :param value: значение
        :return: true, если data ячейки совпадает с value, иначе false.
        """
        return self.data == value


class List:
    """
    Класс для создания односвязных списков.

    Атрибуты:
        head: первый узел списка

        length: длина списка

        node: атрибут для реализации итератора
    Методы:
        get last: Вернуть последний узел списка.

        add_node: Добавить узел в конец списка.


    """

    def __init__(self):
        self.head = None
        self.length = 0
        self.node = None

    def get_last(self) -> Node:
        """
        Вернуть последний узел списка.

        :return: последний узел списка.
        """
        if self.length != 0:
            node = self.head
            while node.next is not None:
                node = node.next
            return node
        raise IndexError("Список пустой.")

    def add_node(self, data) -> None:
        """
        Добавить узел в конец списка.

        :param data: значение добавляемой ячейки.
        """
        self.length += 1
        if not isinstance(data, Node):
            data = Node(data)
        if self.head is None:
            self.head = data
        else:
            self.get_last().next = data

    def output(self) -> None:
        """Вывести содержимое списка."""
        if self.head is None:
            print(None)
        else:
            node = self.head
            while node.next is not None:
                print(node.data)
                node = node.next
            print(node.data)

    def input(self) -> None:
        """Ввести данные в список с клавиатуры."""
        print("Чтобы закончить ввод напишите 'stop'.")
        condition = input()
        while True:
            if condition == "stop":
                answer = input("Закончить ввод? Дайте ответ 'yes' или 'no'.\n")
                if answer == "yes":
                    break
                answer = input("Добавить 'stop' в список? Дайте ответ 'yes' или 'no'.\n")
                if answer == "no":
                    condition = input()
            self.add_node(condition)
            self.length += 1
            condition = input()

    def del_head(self) -> None:
        """Удалить первый элемент списка."""
        self.head = self.head.next
        self.length -= 1

    def del_tail(self) -> None:
        """Удалить последний элемент списка."""
        if self.length == 1:
            self.head = None
            self.length -= 1
        elif self.length > 1:
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None
            self.length -= 1

    def remove(self, value, for_all=False) -> None:
        """
        Удалить первый равный value элемент списка. Удалить все
        элементы списка равные value, если for_all == true.

        :param value: значение удаляемого элемента.
        :param bool for_all: указатель на поведение удаления: удалять все
        элементы равные value или только первый элемент.
        """
        node = self.head
        if node.compare_data(value):
            self.del_head()
            if for_all is False:
                return
        while node.next.next is not None:
            if node.next.compare_data(value):
                node.next = node.next.next
                self.length -= 1
                if for_all is False:
                    return
            node = node.next
        if node.next.compare_data(value):
            node.next = node.next.next
            self.length -= 1

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        node = self.node
        if node is None:
            raise StopIteration
        self.node = self.node.next
        return node.data

    def __getitem__(self, item):
        if self.length >= item:
            node = self.head
            # for _ in range(item-1):
            #     node = node.next
            i = 0
            while i < item:
                node = node.next
                i += 1
            return node.data
        raise IndexError

    def __setitem__(self, key, value):
        if self.length >= key:
            node = self.head
            # for _ in range(key-1):
            #     node = node.next
            i = 0
            while i < key:
                node = node.next
                i += 1
            node.data = value


class HashMap(BaseMap):
    """
    Класс для создания hashmap.

    Атрибуты:
        inner_list: список элементов.

        size: вместимость.

        cnt: количество элементов.
    """

    def __init__(self, _size=10):
        self._inner_list = []
        for _ in range(_size):
            self._inner_list.append(List())
        self._size = _size
        self._cnt = 0

    def get_size(self):
        """
        Вернуть вместимость hashmap.

        :return int _size: вместимость hashmap.
        """
        return self._size

    @property
    def inner_list(self):
        """
        Вернуть список элементов hashmap.

        :return: список элементов hashmap.
        """
        return self._inner_list

    @property
    def cnt(self):
        """
        Вернуть количество элементов hashmap.

        :return: количество элементов hashmap.
        """
        return self._cnt

    def __getitem__(self, key):
        result = self._inner_list[hash(key) % self._size]
        if result.length == 0:
            raise KeyError("Ключ не найден.")
        for i in result:
            if i[0] == key:
                return i[1]
        raise KeyError("Ключ не найден.")

    def __setitem__(self, key, value):
        hash_key = hash(key) % self._size
        if self._inner_list[hash_key].length == 0:
            self._cnt += 1
        flag = True
        for i in range(self._inner_list[hash_key].length):
            if self._inner_list[hash_key][i][0] == key:
                self._inner_list[hash_key][i] = (key, value)
                flag = False
                break
        if flag:
            self._inner_list[hash_key].add_node((key, value))
            if self._cnt >= 0.8 * self._size:
                self._size *= 2
                new_inner_list = List()
                for _ in range(self._size):
                    new_inner_list.add_node(List())
                for i in self._inner_list:
                    if i.length != 0:
                        for j in i:
                            new_inner_list[hash(j[0]) % self._size].add_node(j)
                self._inner_list = new_inner_list
                new_cnt = 0
                for i in self._inner_list:
                    if i.length != 0:
                        new_cnt += 1
                self._cnt = new_cnt

    def __delitem__(self, key):
        deleted = self[key]
        self._inner_list[hash(key) % self._size].remove((key, deleted))
        if self._inner_list[hash(key) % self._size].length == 0:
            self._cnt -= 1

    def __len__(self):
        temp = 0
        for _ in self:
            temp += 1
        return temp

    def __iter__(self):
        temp = []
        for i in self._inner_list:
            for j in i:
                temp.append(j)
        return temp.__iter__()

    def __bool__(self):
        return len(self) != 0

    def clear(self):
        """Очистка экземпляра HashMap"""
        self._size = 10
        self._cnt = 0
        self._inner_list = List()
        for _ in range(10):
            self._inner_list.add_node(List())

    def set_from_list(self, lis):
        """Добавить в мапу элементы из списка, где каждый элемент
        это итерируемый объект из ключа и значения"""
        self.clear()
        for i in lis:
            self[i[0]] = i[1]

#
# if __name__ == "__main__":
#     test = HashMap()
#     test[40] = 1
#     test[30] = 2
#     test[10] = 4
#     test[20] = 6
#     test.write(r"D:\For_Python\informatics_two_term_Kharin_Ildar\testtest.txt")
#     aboba = HashMap.read(r"D:\For_Python\informatics_two_term_Kharin_Ildar\testtest.txt")
#     for i in test:
#         print(i)
#     print(len(test))
#     test._inner_list[0].output()

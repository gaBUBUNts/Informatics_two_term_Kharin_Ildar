def summa(a):
    a = str(a)
    rez = 0
    for i in a:
        rez += int(i)
    return rez


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def compare_data(self, value):
        return self.data == value


class List:
    def __init__(self):
        self.head = None
        self.length = 0
        self.node = None

    def get_last(self):
        if self.length != 0:
            node = self.head
            while node.next is not None:
                node = node.next
            return node

    def add_node(self, data):
        self.length += 1
        if not isinstance(data, Node):
            data = Node(data)
        if self.head is None:
            self.head = data
        else:
            self.get_last().next = data

    def search(self, value):
        node = self.head
        while node.next is not None:
            if node.compare_data(value):
                return True
            node = node.next
        if node.compare_data(value):
            return True
        return False

    def output(self):
        if self.head is None:
            print(None)
        else:
            node = self.head
            while node.next is not None:
                print(node.data)
                node = node.next
            print(node.data)

    def input(self):
        print("Чтобы закончить ввод напишите 'stop'.")
        condition = input()
        while True:
            if condition == "stop":
                print("Закончить ввод? Дайте ответ 'yes' или 'no'.")
                answer = input()
                if answer == "yes":
                    break
                else:
                    print("Добавить 'stop' в список? Дайте ответ 'yes' или 'no'.")
                    answer = input()
                    if answer == "no":
                        condition = input()
            self.add_node(condition)
            self.length += 1
            condition = input()

    def max(self):
        rez = self.head.data
        node = self.head
        while node.next is not None:
            if rez < node.next.data:
                rez = node.next.data
            node = node.next
        return rez

    def sum(self):
        rez = self.head.data
        node = self.head
        while node.next is not None:
            rez += node.next.data
            node = node.next
        return rez

    def check_negative(self):
        node = self.head
        if node.data < 0:
            return True
        while node.next is not None:
            if node.next.data < 0:
                return True
            node = node.next
        return False

    def del_head(self):
        self.head = self.head.next
        self.length -= 1

    def del_tail(self):
        if self.length == 1:
            self.head = None
            self.length -= 1
        elif self.length > 1:
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None
            self.length -= 1

    def del_penultimate(self):
        if self.length == 2:
            self.del_head()
            self.length -= 1
        elif self.length > 2:
            node = self.head
            while node.next.next.next is not None:
                node = node.next
            node.next = node.next.next
            self.length -= 1

    def remove(self, value, for_all=False):
        node = self.head
        if node.compare_data(value):
            self.del_head()
            self.length -= 1
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

    def border(self, value, fringing):
        node = self.head
        if node.compare_data(value):
            self.head = Node(fringing, node)
            node.next = Node(fringing, node.next)
        while node.next is not None:
            if node.next.compare_data(value):
                node.next.next = Node(fringing, node.next.next)
                node.next = Node(fringing, node.next)
                return
            node = node.next
        self.length += 2

    def reverse(self):
        new_list = List()
        for i in range(self.length):
            new_list.add_node(self.get_last())
            self.del_tail()
        self.head = new_list.head

    def input_file(self):
        file_name = input("Введите имя файла: ")
        with open(file_name) as file:
            while True:
                try:
                    self.add_node(int(file.readline()))
                except:
                    break

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        node = self.node
        if node is None:
            raise StopIteration
        self.node = self.node.next
        return node.data


class HashMap:
    class InnerLinkedList:
        pass

    def __init__(self, _size):
        self._inner_list = [None] * _size
        # self. _inner_list = List()
        self._size = _size
        self._cnt = 0

    def __getitem__(self, key):
        return self._inner_list[hash(key) % self._size][1]

    def __setitem__(self, key, value):
        self._inner_list[hash(key) % self._size] = (key, value)
        self._cnt += 1
        if self._cnt >= 0.8 * self._size:
            self._size *= 2
            new_inner_list = [None] * self._size
            for i in self._inner_list:
                if i is not None:
                    new_inner_list[hash(i[0]) % self._size] = i
            self._inner_list = new_inner_list

class Node:
    def __init__(self, data=None, next_node=None, prev=None):
        self.data = data
        self.next = next_node
        self.prev = prev

    def compare_data(self, value) -> bool:
        return self.data == value


class List:
    def __init__(self):
        self.head = None
        self.length = 0
        self.node = None
        self.tail = None
        self.cnt = 0

    def get_last(self) -> Node:
        if self.length != 0:
            return self.tail
        raise IndexError("Список пустой.")

    def add_node(self, data) -> None:
        self.length += 1
        if not isinstance(data, Node):
            data = Node(data)
        if self.head is None:
            data.next = data
            self.head = data
            self.tail = data
        else:
            temp = self.tail
            self.tail.next = data
            self.tail = self.tail.next
            self.tail.prev = temp
            self.tail.next = self.head

    def del_head(self) -> None:
        self.head = self.head.next
        self.head.prev = None
        self.tail.next = self.head
        self.length -= 1

    def del_tail(self) -> None:
        if self.length == 1:
            self.head = None
            self.length -= 1
        elif self.length > 1:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.length -= 1

    def __iter__(self):
        self.node = self.head
        self.cnt = 0
        return self

    def __next__(self):
        node = self.node
        if self.cnt == self.length:
            raise StopIteration
        self.cnt += 1
        self.node = self.node.next
        return node.data

    def __getitem__(self, item):
        if self.length >= item:
            node = self.head
            i = 0
            while i < item:
                node = node.next
                i += 1
            return node.data
        raise IndexError

    def __setitem__(self, key, value):
        if self.length >= key:
            node = self.head
            i = 0
            while i < key:
                node = node.next
                i += 1
            node.data = value


class PlagiatInt:
    def __init__(self, number, sign=None):
        if isinstance(number, List):
            self.num = List
            self.sign = sign
            return
        self.num = List()
        self.sign = "+"
        num = str(number)
        if num[0] == "-":
            self.sign = "-"
            num = num[1:]
        num = num[::-1]
        for i in num:
            #print(i)
            self.num.add_node(int(i))

    def __add__(self, other):
        result = List()
        if self.sign == other.sign:
            if self.num.length >= other.num.length:
                one = self.num
                two = other.num
            else:
                two = self.num
                one = other.num
            for _ in range(one.length + 1):
                result.add_node(0)
            for i in range(one.length):
                if i < two.length:
                    rez = one[i] + two[i]
                else:
                    rez = result[i] + one[i]
                result[i] = 0
                result[i] += rez
                if rez >= 10:
                    result[i] -= 10
                    result[i+1] += 1
            if result.tail.data == 0:
                result.del_tail()
            return PlagiatInt(result, self.sign)

    def __sub__(self, other):
        pass

    def __neg__(self):
        if self.sign == "-":
            return PlagiatInt(self.num, "+")
        return PlagiatInt(self.num, "-")

    def __eq__(self, other):
        for i in self.num:
            for j in other.num:
                if i != j:
                    return False
        return True

    def __ne__(self, other):
        if self == other:
            return False
        return True

    def __lt__(self, other):
        if self.num.length > other.num.length:
            return False
        if self.num.length < other.num.length:
            return True
        else:
            for i in range(self.num.length-1, -1, -1):
                if self.num[i] > other.num[i]:
                    return False
                if self.num[i] < other.num[i]:
                    return True
                continue
            return False

    def __le__(self, other):
        if self < other or self == other:
            return True
        return False

    def __gt__(self, other):
        if other < self:
            return True
        return False

    def __ge__(self, other):
        if self > other or self == other:
            return True
        return False

    def __str__(self):
        result = ""
        result += self.sign
        for i in range(self.num.length-1, -1, -1):
            result += str(self.num[i])
        return result

    __repr__ = __str__


if __name__ == "__main__":
    on = PlagiatInt(123)
    tw = PlagiatInt(456)
    print(on)
    print(on+tw)
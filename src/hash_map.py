from ClassWorks.CW_15_02_2022 import knot as kn


class HashMap:
    class InnerLinkedList:
        pass

    def __init__(self, _size):
        self._inner_list = [None] * _size
        # self. _inner_list = kn.List()
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


hash_map = HashMap(10)
for i in range(15):
    hash_map[i] = i
    print(hash_map._inner_list)

print(hash_map._size, hash_map[14])

op = kn.List()
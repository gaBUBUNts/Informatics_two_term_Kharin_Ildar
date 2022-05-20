"""Модуль с абстрактным классом для различных map."""

from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class BaseMap(ABC):
    """Класс для создания классов map"""
    @abstractmethod
    def __setitem__(self, key: str, value: int) -> None:
        ...

    @abstractmethod
    def __getitem__(self, key: str) -> int:
        ...

    @abstractmethod
    def __delitem__(self, key: str) -> None:
        ...

    @abstractmethod
    def __iter__(self) -> Iterable[Tuple[str, int]]:
        ...

    def __contains__(self, key: str) -> bool:
        try:
            self[key]
        except KeyError:
            return False
        return True

    def __eq__(self, other: 'BaseMap') -> bool:
        for key, value in self:
            try:
                if other[key] == value:
                    continue
                return False
            except KeyError:
                return False
        return True

    @abstractmethod
    def __bool__(self) -> bool:
        ...

    @abstractmethod
    def __len__(self):
        ...

    def items(self) -> Iterable[Tuple[str, int]]:
        """ D.items() -> a set-like object providing a view on D's items """
        yield from self

    def values(self) -> Iterable[int]:
        """ D.values() -> an object providing a view on D's values """
        return (item[1] for item in self)

    def keys(self) -> Iterable[str]:
        """ D.keys() -> a set-like object providing a view on D's keys """
        return (item[0] for item in self)

    @classmethod
    def fromkeys(cls, iterable, value=None) -> 'BaseMap':
        """ Create a new dictionary with keys from iterable and values set to value. """
        result = cls()
        for key in iterable:
            result[key] = value
        return result

    def update(self, other=None) -> None:
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        if other is not None:
            if hasattr(other, "keys"):
                for key in other.keys():
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value

    def get(self, key, default=None):
        """ Получить значение элемента по его ключу. """
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key, default=None):
        """ Удалить элемент по ключу и вернуть его значение. """
        if key in self.keys():
            temp = self[key]
            del self[key]
            return temp
        if default is not None:
            return default
        raise KeyError

    def popitem(self):
        """
        Remove and return a (key, value) pair as a 2-tuple.

        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """
        if self:
            result = tuple()
            for key, value in self:
                result = (key, value)
            del self[result[0]]
            return result
        raise KeyError

    def setdefault(self, key, default=None):
        """
        Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default.
        """
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default

    @abstractmethod
    def clear(self):
        """ D.clear() -> None.  Remove all items from D. """
        print("")

    def write(self, path: str) -> None:
        """ Сериализировать из объекта класса в текстовый файл. """
        with open(path, "w", encoding="utf-8") as file:
            for key, data in self:
                file.write(f"{key}\t{data}\n")

    @classmethod
    def read(cls, path: str) -> 'BaseMap':
        """ Сериализировать из текстового файла в объект класса. """
        my_obj = cls()
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                if line != "":
                    line = line.split("\t")
                    my_obj[line[0]] = int(line[1])
        return my_obj

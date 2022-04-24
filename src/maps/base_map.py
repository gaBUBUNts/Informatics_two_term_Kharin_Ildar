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
        """Функция"""
        yield from self

    def values(self) -> Iterable[int]:
        """Функция"""
        return (item[1] for item in self)

    def keys(self) -> Iterable[str]:
        """Функция"""
        return (item[0] for item in self)

    @classmethod
    def fromkeys(cls, iterable, value=None) -> 'BaseMap':
        """Функция"""
        result = cls()
        for key in iterable:
            result[key] = value
        return result

    def update(self, other=None) -> None:
        """Функция"""
        if other is not None:
            if hasattr(other, "keys"):
                for key in other.keys():
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value

    def get(self, key, default=None):
        """Функция"""
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key, default=None):
        """Функция"""
        try:
            temp = self[key]
            del self[key]
            return temp
        except KeyError:
            if default is not None:
                return default
            raise KeyError

    def popitem(self):
        """Функция"""
        if self:
            result = tuple()
            for key, value in self:
                result = (key, value)
            del self[result[0]]
            return result
        raise KeyError

    def setdefault(self, key, default=None):
        """Функция"""
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default

    @abstractmethod
    def clear(self):
        """Функция"""
        print("")

    def write(self, path: str) -> None:
        """Write something."""
        with open(path, "w", encoding="utf-8") as file:
            for key, data in self:
                file.write(f"{key}\t{data}\n")

    @classmethod
    def read(cls, path: str) -> 'BaseMap':
        """Write something."""
        my_obj = cls()
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                if len(line) != 0:
                    line = line.split("\t")
                    my_obj[line[0]] = int(line[1])
        return my_obj

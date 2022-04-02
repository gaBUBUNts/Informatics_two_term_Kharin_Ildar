"""Модуль с абстрактным классом для различных map."""


from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class BaseMap(ABC):
    """Абстрактный класс для создания классов различных map."""

    @abstractmethod
    def __getitem__(self, key: str) -> int:
        ...

    @abstractmethod
    def __setitem__(self, key: str, value: int) -> None:
        ...

    @abstractmethod
    def __delitem__(self, key) -> None:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __iter__(self) -> Iterable[Tuple]:
        ...

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
                    line.split("\t")
                    my_obj[line[0]] = int(line[1])

        return my_obj


if __name__ == '__main__':
    pass

""" Модуль для тестирования функций слияния файлов. """
import os
import filecmp
import pytest
from src.parsers.merge_files import merge, multi_merge

PATH = r"D:\For_Python\Informatics_two_term_Kharin_Ildar\src\merge"


@pytest.mark.parametrize("paths_of_files", [[os.path.join(PATH, "file1.txt"),
                                             os.path.join(PATH, "file2.txt"),
                                             os.path.join(PATH, "file3.txt"),
                                             os.path.join(PATH, "file12.txt"),
                                             os.path.join(PATH, "merge_file.txt")]])
class TestMergeFiles:
    """ Класс для тестирования функций merge и multi_merge на одном наборе данных. """

    @staticmethod
    def test_merge(paths_of_files):
        """ Тестирование функции merge. """
        merge(paths_of_files[0],
              paths_of_files[1],
              os.path.join(PATH, "test_file_1.txt"))
        assert filecmp.cmp(os.path.join(PATH, "test_file_1.txt"),
                           paths_of_files[3], shallow=False)

    @staticmethod
    def test_multi_merge(paths_of_files):
        """ Тестирование функции multi_merge """
        multi_merge(paths_of_files[:3],
                    os.path.join(PATH, "test_file_2.txt"))
        assert filecmp.cmp(os.path.join(PATH, "test_file_2.txt"),
                           paths_of_files[4], shallow=False)

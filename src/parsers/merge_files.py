"""Модуль для слияния файлов с подсчетом слов, создаваемых функцией wiki_parser"""
import uuid
import os


def merge(path1, path2, path):
    """
    Объединить два файла в один.

    :param path1: путь к первому объединяемому файлу.
    :param path2: путь ко второму объединяемому файлу.
    :param path: путь к файлу, получившемуся в результате слияния двух файлов.
    """
    with open(path, "w", encoding="utf-8") as file:
        with open(path1, "r", encoding="utf-8") as file1:
            with open(path2, "r", encoding="utf-8") as file2:
                line_from_file1 = file1.readline()
                line_from_file2 = file2.readline()
                while True:
                    if line_from_file1 == "" and line_from_file2 == "":
                        break
                    if line_from_file1 == "":
                        while line_from_file2 != "":
                            file.write(line_from_file2)
                            line_from_file2 = file2.readline()
                        break
                    if line_from_file2 == "":
                        while line_from_file1 != "":
                            file.write(line_from_file1)
                            line_from_file1 = file1.readline()
                        break
                    if line_from_file1.split("\t")[0] < line_from_file2.split("\t")[0]:
                        file.write(line_from_file1)
                        line_from_file1 = file1.readline()
                    elif line_from_file1.split("\t")[0] > line_from_file2.split("\t")[0]:
                        file.write(line_from_file2)
                        line_from_file2 = file2.readline()
                    else:
                        temp1 = line_from_file1.split("\t")
                        temp2 = line_from_file2.split("\t")
                        file.write(temp1[0] + "\t" + str(int(temp1[1]) + int(temp2[1])) + "\n")
                        line_from_file1 = file1.readline()
                        line_from_file2 = file2.readline()


def multi_merge(paths, path):
    """
    Объединить файлы в один.

    :param paths: список путей к объединяемым файлам.
    :param path: путь к файлу, получившемуся в результате слияния двух файлов.
    """
    temp_path = path[:-4]
    paths_to_del = []
    while len(paths) > 2:
        curr_paths = []
        len_paths = len(paths)
        for i in range(0, len_paths - len_paths % 2, 2):
            temp = temp_path + uuid.uuid4().hex + ".txt"
            paths_to_del.append(temp)
            curr_paths.append(temp)
            merge(paths[i], paths[i + 1], temp)
        if len_paths % 2 == 1:
            curr_paths.append(paths[-1])
            paths = curr_paths
        else:
            paths = curr_paths
    merge(paths[0], paths[1], path)
    for i in paths_to_del:
        os.remove(i)

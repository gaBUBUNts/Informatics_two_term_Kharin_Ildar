"""
Модуль для подсчета слов на странице вики.

Результат сохраняется в файл word.txt по указанному пути.
"""

import os
import uuid
import re
from time import sleep, time
import requests as req
import bs4 as bs
from src.maps.hash_map import HashMap


def timer_func(func):
    """Декоратор, замеряющий время выполнения функции"""

    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Function {func.__name__!r} executed in {(end - start):.4f}s')
        return result

    return wrap_func


def convert_to_word(string):
    """
    Функция конвертации строки в слова

    :param string:строка, содержащая слова
    :return:слова из строки без специальных символов
    """
    string = string.replace(".", "")
    string = string.replace(":", "")
    string = string.replace(";", "")
    string = string.replace(",", "")
    string = string.replace("«", "")
    string = string.replace("»", "")
    temp = []
    for word in string.split():
        if word[0] in r"""`~1234567890!@#$%^&*()-=_+[]{}\|/,.?'"№:;""":
            temp.append(None)
        else:
            temp.append(word)
    return temp


def add_base_path(base_path):
    """Функция для создания родительской папки для функции wiki_parser"""
    if os.path.exists(base_path):
        print("Создание не удалось: папка base_path уже создана.\n", end="")
    else:
        os.mkdir(base_path)
        print("Папка base_path создана.\n", end="")


def wiki_parser(url: str, base_path):
    """
    Функция для подсчета слов на странице википедии.

    :param str url: адрес страницы вики.
    :param str base_path: путь к папке, в которой создастся папка base_path. Это родительская
        папка, в которой будут храниться папки с результатами.
    :return: список ссылок на страницы википедии.
    """
    # Создание родительской папки.
    base_path += "\\base_path"
    add_base_path(base_path)

    # Проверка на наличия url в сохраненных файлах.
    flag = True
    dirlist = os.listdir(base_path)
    path = base_path  # путь до папки с файлами url.txt и content.bin
    for i in dirlist:
        with open(os.path.join(base_path, i, "url.txt"), "r", encoding="utf-8") as url_file:
            if url_file.read() == url:
                flag = False
                path = os.path.join(path, i)
                print("_____поиск url завершен, url уже был обработан_____\n", end="")
                break
    print("поиск url завершен, url еще не был обработан\n", end="")
    # Если url не нашелся, то создать папку с файлами url.txt, content.bin
    if flag:
        path = os.path.join(path, uuid.uuid4().hex)
        os.mkdir(path)
        with open(os.path.join(path, "url.txt"), "w", encoding="utf-8") as url_file:
            url_file.write(url)
        text = req.request("GET", url).content
        with open(os.path.join(path, "content.bin"), "wb") as content_file:
            content_file.write(text)

        print("_____url обработан_____\n", end="")
    # Подсчет слов с помощью HashMap. Сериализация HashMap в файл words.txt
    if not os.path.exists(os.path.join(path, "content.bin")):
        while True:
            sleep(0.1)
            if os.path.exists(os.path.join(path, "content.bin")):
                break
    with open(os.path.join(path, "content.bin"), "rb") as content_file:
        soup = bs.BeautifulSoup(content_file, "lxml")
        hash_map = HashMap()
        for string in soup.stripped_strings:
            for word in convert_to_word(string):
                if word is None:
                    continue
                try:
                    hash_map[word] += 1
                except KeyError:
                    hash_map[word] = 1
        hash_map.write(os.path.join(path, "words.txt"))
        # Вернуть список всех ссылок на вики.
        href_list = []
        for tag in soup.find_all(href=re.compile("^/wiki/")):
            href_list.append("https://ru.wikipedia.org" + tag["href"])
        print("__________выполнение закончено__________\n", end="")
        return href_list


if __name__ == "__main__":
    rez = wiki_parser('https://ru.wikipedia.org/wiki/Чёрмозский_завод',
                      r'D:\For_Python\Informatics_two_term_Kharin_Ildar\src')
    for j in rez:
        print(j)

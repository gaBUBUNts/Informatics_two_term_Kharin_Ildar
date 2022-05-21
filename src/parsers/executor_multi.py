"""Модуль для многопоточного или многопроцессорного выполнения функции wiki_parser"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from itertools import repeat
from parsers.wiki_parser import wiki_parser, timer_func


@timer_func
def multi(mode, url, base_path, max_workers=5, deep=3):
    """
    Функция, выполняющая функцию wiki_parser многопоточно или многопроцессорно.

    :param mode: режим выполнения: многопоточный/многопроцессорный
        (ThreadPoolExecutor/ProcessPoolExecutor)
    :param url: первая обрабатываемая функцией wiki_parser ссылка
    :param base_path: путь к родительской папке
    :param deep: глубина переходов по ссылкам
    :param max_workers: максимальное количество потоков или процессов
    """
    beginning = wiki_parser(url, base_path)
    for _ in range(deep - 2):
        executor = mode(max_workers=max_workers)
        temp = []
        futures = [executor.submit(wiki_parser, url, path)
                   for url, path in zip(beginning, repeat(base_path))]
        for i in futures:
            temp += i.result()
        beginning = temp
        executor.shutdown()


if __name__ == "__main__":
    multi(ThreadPoolExecutor, 'https://ru.wikipedia.org/wiki/Чёрмозский_завод',
          r'D:\For_Python\Informatics_two_term_Kharin_Ildar\src')
    multi(ProcessPoolExecutor, 'https://ru.wikipedia.org/wiki/Чёрмозский_завод',
          r'D:\For_Python\Informatics_two_term_Kharin_Ildar\src')

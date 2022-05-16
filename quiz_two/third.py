import threading as thr
import time
import random

t1 = time.time()
tasks_id = [i for i in range(20)]


def get_data(task_id):
    print(f"processing get_data({task_id})\n", end="")
    time.sleep(random.randint(1, 3))
    print(f"completed get_data({task_id})\n", end="")


def write_to_file(task_id):
    print(f"processing write_to_file({task_id})\n", end="")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_file({task_id})\n", end="")


def write_to_console(task_id):
    print(f"processing write_to_console({task_id})\n", end="")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_console({task_id})\n", end="")


sem1 = thr.BoundedSemaphore(10)
sem2 = thr.BoundedSemaphore(5)
sem3 = thr.BoundedSemaphore(1)


def new_get_data(task_id):
    with sem1:
        get_data(task_id)


def new_write_to_file(task_id):
    with sem2:
        write_to_file(task_id)


def new_write_to_console(task_id):
    with sem3:
        write_to_console(task_id)


def use_funcs(task_id):
    new_get_data(task_id)
    thr1 = thr.Thread(target=new_write_to_console, args=(task_id,))
    thr2 = thr.Thread(target=new_write_to_file, args=(task_id,))
    thr1.start()
    thr2.start()


thrs = []
for i in range(20):
    thrs.append(thr.Thread(target=use_funcs, args=(tasks_id[i],), name=f"{i}"))
for i in thrs:
    i.start()

while thr.active_count() > 1:
    continue

print(time.time() - t1)

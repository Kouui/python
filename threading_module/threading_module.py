#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         MIT-license
#
# Title: threading_module             Version: 1.0
# Date: 26-12-16                      Language: python3
# Description: meerdere threats per keer uitvoeren
#
###############################################################
# todo verder uitzoeken hoe threading werkt !
import threading
from queue import Queue
import time

print_lock = threading.Lock()

def example_job(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, worker)

def  threader ():
    while True:
        worker  = q.get()
        example_job(worker)
        q.task_done()

q = Queue()

for x in range(10):
    t = threading.Thread(target=threader)
    t.daemon=  True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('entire job took:', time.time() -start)
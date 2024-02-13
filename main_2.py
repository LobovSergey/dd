from random import randint
import numpy as np
import time
from data import *
from utils import teachers_data

now = time.time()

RANDOM_CASE = [[randint(1, WINDOW) for _ in range(LONG)] for _ in range(5)]
TEST_CASE = teachers_data
CASE = np.array(RANDOM_CASE)
DEEP = len(TEST_CASE)


def search(head=[], i=0):
    print(f"CURRENT {i}")
    shedule = TEST_CASE[i].lessons_list
    for _ in range(COUNTER):
        np.random.shuffle(shedule)
        print(f"SEARCHED {i+1}")
        if i == 0:
            response = search(head=shedule, i=i+1)
            if type(response) is not tuple:
                return response
        else:
            result_b = np.not_equal(head, shedule)
            result_uni = np.unique(result_b)
            if len(result_uni) and result_uni[0]:
                combination = np.vstack([head, shedule])
                if i == DEEP - 1:
                    return combination
                result = search(i=i+1, head=combination)
                if type(result) is tuple:
                    continue
                return result
    return (None, False)


res = search()
print("____________")
if type(res) is not tuple:
    print(res)
else:
    print("NO COMB")
end = time.time()
time_result = end - now
print(time_result * 1000)

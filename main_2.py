from random import randint, shuffle
import numpy as np
import time
from data import *
from utils import teachers_data

now = time.time()

RANDOM_CASE = [[randint(1, WINDOW) for _ in range(LONG)] for _ in range(5)]
TEST_CASE = teachers_data
CASE = np.array(RANDOM_CASE)
DEEP = len(TEST_CASE)



def search(head=[], i=1):
    print(f"CURRENT {i}")
    shedule = TEST_CASE[i-1].lessons_list
    C = COUNTER * i * i
    for _ in range(C):
        np.random.shuffle(shedule)
        print(f"SEARCHED {i+1}")
        if i == 1:
            response = search(head=shedule, i=i+1)
            if type(response) is not tuple:
                return response
        else:
            result_b = np.not_equal(head, shedule)
            result_uni = np.unique(result_b)
            if len(result_uni) and result_uni[0]:
                combination = np.vstack([head, shedule])
                if i == DEEP:
                    return combination
                result = search(i=i+1, head=combination)
                if type(result) is tuple:
                    continue
                return result
        if _ > (0.2 * C):
            break
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

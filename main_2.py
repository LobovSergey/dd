from random import randint
import numpy as np
import time
from data import *
from utils import teachers_data
 
now = time.time()

RANDOM_CASE = [[randint(1,WINDOW) for _ in range(LONG)] for _ in range(DEEP)]
TEST_CASE = teachers_data
CASE = np.array(RANDOM_CASE)


def search(i=0, stack:list = []):
    for _ in range(COUNTER): 
        shedule = TEST_CASE[i].lessons_list
        np.random.shuffle(shedule)
        print(f"LVL {i+1} - {TEST_CASE[i].id}")
        if i == 0:
            if search(i+1, stack=shedule):
                return True
        else:
            result_b = np.not_equal(stack, shedule)
            result_uni = np.unique(result_b)
            if len(result_uni) and result_uni[0]:
                if i == DEEP - 1:
                    return True
                if search(i+1):
                    return True
    return False


print(teachers_data)
res = search()
print("____________")
if res:
    print(CASE)
else:
    print("NO COMB")
end = time.time()
time_result = end - now
print(time_result * 1000)
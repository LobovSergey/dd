from random import randint
import numpy as np
import time
from data import *

now = time.time()
LONG = 35
DEEP = 17
WINDOW = 100
RANDOM_CASE = [[randint(1,WINDOW) for _ in range(LONG)] for _ in range(DEEP)]
TEST_CASE = [
    CASE_1,
    CASE_2,
    CASE_3,
    CASE_4,
    CASE_5,
    CASE_6,
    CASE_7,
    CASE_8,
    CASE_9,
    CASE_10,
    CASE_11,
    CASE_12,
    CASE_13,
    CASE_14,
    CASE_15,
    CASE_16,
    CASE_17,
    CASE_18,
    CASE_19,    
    CASE_20,
    CASE_21,
    CASE_22,
    CASE_23,
    CASE_24,
    CASE_25,
    CASE_26,
    CASE_27,
    CASE_28,
    CASE_29,
    CASE_30,
    CASE_31,
    CASE_32,
    CASE_33,
    CASE_34,
    CASE_35]
CASE = np.array(RANDOM_CASE)
COUNTER = 10

def search(i=0):
    for _ in range(COUNTER): 
        np.random.shuffle(CASE[i])
        print(f"LVL {i+1} - {CASE[i]}")
        if i == 0:
            if search(i+1):
                return True
        else:
            result_b = np.not_equal(CASE[:i], CASE[i])
            result_uni = np.unique(result_b)
            if len(result_uni) and result_uni[0]:
                if i == DEEP - 1:
                    return True
                if search(i+1):
                    return True
    return False

        

            
    
    
        


     
    



print(CASE)
res = search()
print("____________")
if res:
    print(CASE)
else:
    print("NO COMB")
end = time.time()
time_result = end - now
print(time_result * 1000)
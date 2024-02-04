from collections import Counter
from enum import unique
from sys import api_version
from traceback import print_list
import numpy as np
from itertools import permutations


def find(x,y):
    c = []
    for i in x:
        if i in y:
            c.append(i)
    return c


def sort(a, lis):
    

TEST_CASE_1 = [1,2,3,8]
TEST_CASE_2 = [7,1,8,1]

A_T1 = 
A_T2 = sorted(TEST_CASE_2)

print(A_T1)
print('-----------------------------')
print(A_T2)
print(np.equal(A_T1,A_T2))



a = list(permutations(TEST_CASE_1))
b = list(permutations(TEST_CASE_2))
# ap = np.array(a)
# print(ap)
# print(len(ap))
# bp = np.array(b)
# print('-----------------------------')
# print(bp)
# print(len(bp))
uniqu = 0
u = 0

# for i in ap:
#     for j in bp:
#         res = np.equal(i,j)
#         res_b = np.unique(res)
#         if res_b.size == 1 and not res_b[0]:
#             uniqu += 1
#         u += 1

# print(uniqu)
# print(u)
# print(uniqu/u)
         












        
        









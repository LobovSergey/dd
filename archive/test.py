from random import randint
from re import I
import numpy as np
import pandas as pd
from itertools import permutations

max_hours = 6
max_teachers = 2


def search(el, _list):
    l_list = len(_list)
    if l_list == 1:
        if el == _list[0]:
            return True
        else:
            return False
    i = len(_list) // 2
    if el in _list[0:i]:
        return search(el, _list[:i])
    return search(el, _list[i:])


def chance_combination(l1, l2):
    count = 0
    for i in l1:
        if search(i, l2):
            count += 1

 
for _ in range(1):
    # l = [[randint(0, 9) for _ in range(max_hours)]
    #      for _ in range(max_teachers)]
    # l = [["1b","5c", "2b", "6c","1b", "None"], ["2b","3c", "1b", "5c","4b", "None"] ]
    # jll = list(map(lambda x : sorted(x), l))
    # l = np.array([*jll])
    l1 = [1, 3, 2, 4]
    l2 = [1, 4, 1, 4] 
    l1_p = list(permutations(l1))

    print(len(set(l1)), "uniq")
    print(len(l1), "slots")
    print(len(l1_p), "all")
    print(len(set(l1_p)), "uni combo")
    print(len(set(l1)) / len(l1), "K types")
    print(len(set(l1_p)) / len(l1_p), 'K combos')

    # uni = 0
    # all = 0
    # for i in l1_p:
    #     for j in l2_p:
    #         b_l = np.equal(i,j)
    #         r = np.unique(b_l)
    #         if len(r) == 1 and not r[0]:
    #             uni += 1
    #         all += 1
    # print("res", uni)
    # print("ALL", all)
    # print(uni/all)

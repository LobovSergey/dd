from collections import Counter
from enum import unique
from random import choice, randint
from sys import api_version
from traceback import print_list
import numpy as np
from itertools import permutations

max_hours = 5
max_teachers = 3
l = [[randint(0, 8) for _ in range(max_hours)] for _ in range(max_teachers)]

s = np.array(l)
s.sort()


def sort_matrix(matr):
    coloumn_counter = np.shape(matr)[0]
    r_i = randint(0, coloumn_counter - 1)
    l_s = np.array([[x] for x in matr if x[0] < matr[r_i][0]])
    e_s = np.array([[x] for x in matr if x[0] == matr[r_i][0]])
    g_s = np.array([[x] for x in matr if x[0] > matr[r_i][0]])
    print(l_s)
    print(e_s)
    print(g_s)

    # return np.vstack([sort_matrix(l_s), e_s, sort_matrix(g_s)])


res = sort_matrix(s)
print(res)

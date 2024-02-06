from random import randint
import numpy as np
from itertools import permutations

max_hours = 5
max_teachers = 3
t = 0
f = 0
log = ""


def sort_matrix(matr, index=0):
    print("START WORK WITH", matr)
    rows = np.shape(matr)[0]
    r_i = randint(0, rows - 1)
    l_s = [x for x in matr if x[index] < matr[r_i][index]]
    e_s = [x for x in matr if x[index] == matr[r_i][index]]
    g_s = [x for x in matr if x[index] > matr[r_i][index]]
    print("<", l_s)
    print("=", e_s)
    print(">", g_s)
    grades = [l_s, e_s, g_s]
    print(grades)
    for val in grades:
        if len(val) > 1:
            if np.equal(*val)[index]:
                sort_matrix(val, index + 1)
            else:
                sort_matrix(val, index)
        elif len(val) == 1:
            query.append(val)
    return query


for _ in range(100):
    l = [[randint(0, 9) for _ in range(max_hours)]
         for _ in range(max_teachers)]
    print("START", l)
    l.sort()
    print("SORT", l)

    query = []
    res = sort_matrix(l)
    print(f"\033[32m{res}\033[0m")
    if len(res) == 3:
        t += 1
    else:
        f += 1
        log += f"\n\n{res} \nWITH START\n {l}"

print("TRUE", t)
print("FALSE", f)
input()
print(log)

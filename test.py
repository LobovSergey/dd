from random import  randint
import numpy as np
from itertools import permutations

max_hours = 5
max_teachers = 3
l = [[randint(0, 9) for _ in range(max_hours)] for _ in range(max_teachers)]

s = np.array(l)
s.sort()
print(bool([]))

# def check(*args):
#     for i in args[0]:
#         if i



def sort_matrix(matr, index=0): 
    print("START WORK WITH", matr)
    query = []   
    rows = np.shape(matr)[0]    
    r_i = randint(0, rows - 1)
    l_s = np.array([x for x in matr if x[0] < matr[r_i][0]])
    e_s = np.array([x for x in matr if x[0] == matr[r_i][0]])
    g_s = np.array([x for x in matr if x[0] > matr[r_i][0]])
    print("<", l_s)
    print("=",e_s)
    print(">",g_s)
    grades = [l_s, e_s, g_s]    
    for i in grades:
        if len(i) > 1:
            if index > 5:
                query.append(i)
                print('ДОБАВИЛ ', i)
            else:
                sort_matrix(i, index + 1)
        elif len(i) == 1:            
            query.append(i)
            print('ДОБАВИЛ ', i)
    return query


res = sort_matrix(s)
print(res)


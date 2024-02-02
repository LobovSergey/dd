
# from operator import index
# from random import randint

# import numpy as np

# l = 4


# a = [[[randint(0, l**2) for _ in range(l)] for _ in range(l)] for _ in range(l)] 


# b = map(lambda i: np.array(i), a)
# z = list(b)


# bollean_pair = [(z[i] == z[i+1]) for i in range(len(z)) if i < len(z) - 1]
# print(bollean_pair)



# # for i in range(len(z)):
# #     if i == len(z) - 1:
# #         break
# #     res = (z[i] == z[i+1])
# #     print(res)



# a = []
# if a:
#     print('asd')




from itertools import permutations
from math import factorial
import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8,1]
b = [2, 4]

def comp(i,j):
    pass


n = 4
k = 2
z = factorial(n) / (factorial(k) * factorial(n - k))
print(z)

i_1 = permutations(a)
i_2 = permutations(b)
v = [list(i_1.__next__()) for _ in range(int(z))]
print(np.array(v))

# comp(i=i_1,j=i_2)


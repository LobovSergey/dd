from itertools import permutations
from math import factorial
from random import randint
from typing import Iterable, Iterator
import numpy as np

max_hours = 6
max_teachers = 3


def prepare_data():
    global len_permutation
    global list_permutations
    lessons_list = [[randint(0,3) for _ in range(max_hours)] for _ in range(max_teachers)]
    len_permutation = factorial(max_hours)
    list_permutations = [permutations(teacher_class) for teacher_class in lessons_list]
    





def head_combination(iteration: Iterator):
    head = list(iteration.__next__())
    return head


def combinate(head_combination, *iterations):                
        unpacked_iter = iterations[0]
        iteraton = unpacked_iter[0]             
        for _ in range(len_permutation):
            candidate_row = np.array(list(iteraton.__next__()))        
            res_bool = np.equal(head_combination, candidate_row) 
            unique_bool = np.unique(res_bool)
            if unique_bool.size == 1 and not unique_bool[0]:
                finded_combination = np.vstack([head_combination, candidate_row])
                main_combination = finded_combination
                if len(unpacked_iter) != 1:
                    result = combinate(finded_combination, unpacked_iter[1:])
                    if type(result) == tuple:
                        head_combination = main_combination[:-1:]                         
                        continue                       
                return main_combination
        return (head_combination, 0)
            
def main():                
    while True:
        head = head_combination(iteration=list_permutations[0])
        main_combination = combinate(head, list_permutations[1:])
        if type(main_combination) == tuple:
            continue
        break
    return main_combination


if __name__ == "__main__":
    prepare_data()
    main()

         














        
        









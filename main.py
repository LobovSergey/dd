from itertools import permutations
from math import factorial
from random import randint
import numpy as np

max_hours = 5
max_teachers = 5
TEST_CASE = [[1,2,3],[2,1,3],[3,2,1]]

def prepare_data():
    global len_permutation 
    global lessons_list   
    global head_combination
    lessons_list = [[randint(0,5) for _ in range(max_hours)] for _ in range(max_teachers)]
    # lessons_list = TEST_CASE
    len_permutation = factorial(max_hours)
    head_lessons = lessons_list[0]
    head_combination = permutations(head_lessons)
    # list_permutations = [permutations(teacher_class) for teacher_class in lessons_list]
    





def head_call():
    try:
        head = head_combination.__next__()  
        return head     

    except StopIteration:
        raise StopIteration(f'we dont have combinations with {[print(i) for i in lessons_list]}') 
        


def combinate(head_combination, *lessons):                
        unpacked_lessons = lessons[0]
        lesson = unpacked_lessons[0] 
        iteration = permutations(lesson)            
        for _ in range(len_permutation):
            candidate_row = np.array(list(iteration.__next__()))        
            res_bool = np.equal(head_combination, candidate_row) 
            unique_bool = np.unique(res_bool)
            if unique_bool.size == 1 and not unique_bool[0]:
                finded_combination = np.vstack([head_combination, candidate_row])
                main_combination = finded_combination
                if len(unpacked_lessons) != 1:
                    result = combinate(finded_combination, unpacked_lessons[1:])
                    if type(result) == tuple:
                        head_combination = main_combination[:-1:]                         
                        continue
                    return result                       
                return main_combination
        return (head_combination, 0)
            
def main():                
    while True:
        head = head_call()
        main_combination = combinate(head, lessons_list[1:])
        if type(main_combination) == tuple:
            continue
        break
    return main_combination

def print_result(result):
    print(result)



if __name__ == "__main__":
    prepare_data()
    result = main()
    print_result(result)

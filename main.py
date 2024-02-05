from itertools import permutations
from math import factorial
from random import choice, randint, shuffle
import numpy as np
import time

max_hours = 5
max_teachers = 5
TEST_CASE = [[10, 8, 8], [6, 6, 8], [4, 6, 8]]
# np.array(list(iteration.__next__()))


def prepare_data():
    global len_permutation
    global lessons_list
    global head_combination
    lessons_list = [[randint(0, 8) for _ in range(max_hours)]
                    for _ in range(max_teachers)]
    # lessons_list = TEST_CASE
    len_permutation = factorial(max_hours)
    head_lessons = lessons_list[0]
    head_combination = permutations(head_lessons)
    # list_permutations = [permutations(teacher_class) for teacher_class in lessons_list]


def coefficients(item_1, item_2):
    bool_list = np.equal(item_1, item_2)


def head_call():
    try:
        head = head_combination.__next__()
        return head
    except StopIteration:
        return None


def combinate(head_combination, *lessons):
    print('ПРИШОЛ')
    unpacked_lessons = lessons[0]
    lesson = unpacked_lessons[0]
    iteration = list(permutations(lesson))
    for _ in range(len_permutation):
        candidate_row = choice(iteration)
        res_bool = np.equal(head_combination, candidate_row)
        unique_bool = np.unique(res_bool)
        if unique_bool.size == 1 and not unique_bool[0]:
            finded_combination = np.vstack([head_combination, candidate_row])
            if len(unpacked_lessons) != 1:
                result = combinate(finded_combination, unpacked_lessons[1:])
                if type(result) == tuple:
                    finded_combination = finded_combination[:-1:]
                    continue
                print('УШОЛ')
                return result
            print('УШОЛ')
            return finded_combination
    print('УШОЛ')
    return (head_combination, 0)


def main():
    while True:
        head = head_call()
        if head is None:
            return f"No combination! {lessons_list}"
        main_combination = combinate(head, lessons_list[1:])
        if type(main_combination) == tuple:
            continue
        return main_combination


if __name__ == "__main__":
    now = time.time()
    prepare_data()
    result = main()
    print(result)
    last = time.time()
    print(1000*(last-now))

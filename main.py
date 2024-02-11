from itertools import permutations
from math import factorial
from random import randint
import numpy as np
from math import trunc

import time

max_hours = 4
max_teachers = 4
TEST_CASE = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]


def prepare_data():
    global len_permutation
    global lessons_list
    global head_combination
    # lessons_input = [[randint(0, 8) for _ in range(max_hours)]
    #                  for _ in range(max_teachers)]
    lessons_input = TEST_CASE
    lessons_list = list(map(lambda x: sorted(x), lessons_input))
    lessons_list.sort()
    # lessons_list = TEST_CASE
    len_permutation = factorial(max_hours)
    head_lessons = lessons_list[0]
    head_combination = permutations(head_lessons)
    # list_permutations = [permutations(teacher_class) for teacher_class in lessons_list]


def skipper(index, iter, flag, frame_index):
    if index != frame_index:
        iter.__next__()
        return
    flag = True


def frame_finder(b_list: list[bool]):
    ki = 1
    if b_list[0]:
        ki = 1 / max_hours
        return trunc(len_permutation * ki)
    return 1


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
    iterations = permutations(lesson)
    flag = True
    for index in range(len_permutation):
        if not flag:
            skipper(index, iterations, flag, frame)
            continue
        candidate_row = iterations.__next__()
        res_bool = np.equal(head_combination, candidate_row)
        frame_finder(res_bool)
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

from itertools import permutations
import pandas as pd


CLASS_ONE_LIST = ['1a', '2b', '3a']
CLASS_TWO_LIST = ['1b', '3a']
HOURS = 7
REPEATS_ONE_LIST = [2, 2, 1]
REPEATS_TWO_LIST = [2, 2]


def permutation_lessons(types_class, repeats, max_hours):
    all = list(zip(types_class, repeats))
    week_lessons = [x[0] for x in all for _ in range(x[1])]

    while len(week_lessons) != max_hours:
        week_lessons.append(None)

    x = permutations(week_lessons)
    return list(x)


def combine_teachers_lessons(first_combinations, second_combinations, result: list = []):
    for i in first_combinations:
        for j in second_combinations:
            counter = 0
            for index in range(HOURS):
                if i[index] == j[index]:
                    if (i[index] is not None) and (j[index] is not None):
                        break
                counter += 1
            # if counter == HOURS:
            #     print(pd.array(i, j))


f_teacher = permutation_lessons(
    types_class=CLASS_ONE_LIST, repeats=REPEATS_ONE_LIST, max_hours=HOURS)
s_teacher = permutation_lessons(
    types_class=CLASS_TWO_LIST, repeats=REPEATS_TWO_LIST, max_hours=HOURS)


result_combinations = combine_teachers_lessons(f_teacher, s_teacher)
print(pd.array())

import json
from data import LONG
from lesson_class import Lesson


with open('data.json', "r", encoding="UTF-8") as f:
    file = json.load(f)

DATA_FILE = file["teachers"]

teachers_data = [
    Lesson(
        id=var["id"],
        teacher=var["info"]["name"],
        group=var["info"]["group"],
        discipline=var["info"]["discipline"],
        lessons=var["info"]["lessons"]        
    ) for var in DATA_FILE
]



for i in teachers_data:
    i.set_lesson_list()
    print(i)
    print(len(i.lessons_list))
    i.add_windows(max_lessons=LONG)
    print(i)
    print(len(i.lessons_list))
    print("_____________")
    
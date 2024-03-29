import json
from data import LONG
from lesson_class import Lesson


with open('data_test.json', "r", encoding="UTF-8") as f:

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
    i.setup_data()

teachers_data.sort(key=lambda x: x.hours, reverse=False)

print(len(teachers_data))
print(teachers_data)


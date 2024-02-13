
from dataclasses import dataclass, field
from random import randint
from secrets import randbelow

from data import LONG


@dataclass
class Lesson:
    id: int = -1
    teacher: str = ""
    group: bool = False
    discipline: str = "window"
    lessons: dict = field(default_factory=dict)
    lessons_list: list = field(default_factory=list)
    hours: int = 0

    def __repr__(self):
        return f"{self.teacher}"

    def get_lessons(self):
        return self.lessons

    def get_group(self):
        return self.group

    def _set_lesson_list(self):
        self.lessons_list = [key for key, val in self.lessons.items()
                             for _ in range(val)]

    def _add_windows(self, max_lessons):
        while len(self.lessons_list) < max_lessons:
            self.lessons_list.append(f"None {self.id}")

    def _set_hours(self):
        self.hours = len(self.lessons_list)

    def setup_data(self):
        self._set_lesson_list()
        self._set_hours()
        self._add_windows(max_lessons=LONG)

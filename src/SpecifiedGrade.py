# -*- coding: utf-8 -*-
from NotFoundException import NotFoundException
from Types import DataType
import Constant


class SpecifiedGrade:
    def __init__(self, data: DataType):
        self.data: DataType = data

    def identify(self) -> str:
        student_with_good_academic_performance = []
        for student in self.data:
            count_good_ratings = 0
            for subject in self.data[student]:
                if subject[1] == Constant.GRADE:
                    count_good_ratings += 1

            if count_good_ratings >= Constant.MIN_NUMBER_SPECIFIED_GRADE:
                student_with_good_academic_performance.append(student)

        if len(student_with_good_academic_performance) == 0:
            raise NotFoundException(f"Студенты с указаным кол-вом"
                                    f" ({Constant.MIN_NUMBER_SPECIFIED_GRADE})"
                                    f" оценки {Constant.GRADE} не найдены")

        return student_with_good_academic_performance[0]

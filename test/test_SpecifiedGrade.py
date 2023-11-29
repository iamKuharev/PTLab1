from src.NotFoundException import NotFoundException

from src.Types import DataType
from src.SpecifiedGrade import SpecifiedGrade
import pytest
import Constant


class TestSpecifiedGrade:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, str]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ],
            "Сидоров Андрей Владимирович":
                [
                    ("математика", 76),
                    ("русский язык", 76),
                    ("программирование", 76),
                    ("литература", 97)
                ]
        }

        full_name: str = "Сидоров Андрей Владимирович"
        return data, full_name

    def test_init_specified_grade(
            self, input_data: tuple[DataType, str]) -> None:
        calc_rating = SpecifiedGrade(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_identify(
            self, input_data: tuple[DataType, str]) -> None:
        full_name = SpecifiedGrade(input_data[0]).identify()
        assert full_name == input_data[1]

    def test_more_than_one_student_who_fits_the_conditions(self) -> None:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 76),
                    ("русский язык", 76),
                    ("программирование", 76),
                    ("литература", 76)
                ],
            "Сидоров Андрей Владимирович":
                [
                    ("математика", 76),
                    ("русский язык", 76),
                    ("программирование", 76),
                    ("литература", 97)
                ]
        }
        full_name = SpecifiedGrade(data).identify()
        assert full_name == "Петров Игорь Владимирович"

    def test_not_student_who_fits_the_conditions(self) -> None:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 76),
                    ("русский язык", 6),
                    ("программирование", 76),
                    ("литература", 90)
                ]
        }
        sg = SpecifiedGrade(data)
        with pytest.raises(Exception) as e:
            sg.identify()

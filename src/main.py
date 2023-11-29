import argparse
import sys
import os

from CalcRating import CalcRating
from SpecifiedGrade import SpecifiedGrade
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader

from NotFoundException import NotFoundException


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    filename = os.path.basename(path)
    extension = os.path.splitext(filename)[-1].lower()

    students = {}
    if extension == ".txt":
        reader = TextDataReader()
        students = reader.read(path)
        print("Students: ", students)
    elif extension == ".yaml":
        reader_yaml = YamlDataReader()
        students = reader_yaml.read(path)
        print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    try:
        full_name_student = SpecifiedGrade(students).identify()
        print("Full name: ", full_name_student)
    except NotFoundException as exp:
        print(exp)


if __name__ == "__main__":
    main()

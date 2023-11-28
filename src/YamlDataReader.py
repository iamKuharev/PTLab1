from Types import DataType
from DataReader import DataReader
import yaml


class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, "r") as stream:
            data = yaml.safe_load(stream)
            for item in data:
                for key in item:
                    self.key = str(key)
                    self.students[self.key] = []
                    scores = item[key]
                    for score_key in scores:
                        self.students[self.key].append(
                            (score_key, int(scores[score_key])))
        return self.students

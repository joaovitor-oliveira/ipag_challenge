from abc import ABC


class Shape(ABC):

    def calculate_area():
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

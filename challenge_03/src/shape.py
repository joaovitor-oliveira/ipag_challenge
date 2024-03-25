from abc import ABC, abstractmethod


class Shape(ABC):
    '''A shape abstraction.'''
    @abstractmethod
    def calculate_area(self):
        '''Must be implemented.'''
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        '''Must be implemented.'''
        raise NotImplementedError

from abc import ABC, abstractmethod


class TVInterface(ABC):
    '''TV interface.'''

    @abstractmethod
    def is_enable(self):
        '''Must be implemented.'''
        ...

    @abstractmethod
    def enable(self):
        '''Must be implemented.'''
        ...

    @abstractmethod
    def disable(self):
        '''Must be implemented.'''
        ...

    @abstractmethod
    def get_brand(self):
        '''Must be implemented.'''
        ...

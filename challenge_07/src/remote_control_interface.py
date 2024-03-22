from abc import ABC, abstractmethod


class RemoteControlInterface(ABC):
    '''Remote Control Interface.'''
    @abstractmethod
    def toggle_power(self):
        '''Must be implemented.'''
        ...

    @abstractmethod
    def validate(self):
        '''Must be implemented.'''
        ...

from abc import ABC, abstractmethod


class RemoteControlInterface(ABC):
    '''Remote control interface.'''

    @abstractmethod
    def toggle_power(self):
        '''Must be implemented.'''
        ...

    @abstractmethod
    def validate(self):
        '''Must be implemented.'''
        ...

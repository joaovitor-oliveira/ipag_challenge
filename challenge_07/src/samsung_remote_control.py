from challenge_07.src.remote_control_interface import RemoteControlInterface
from challenge_07.src.tv_interface import TVInterface
from challenge_07.src.brand import Brand
from challenge_07.src.brand_exception import BrandException
from dataclasses import dataclass


@dataclass
class SamsungRemoteControl(RemoteControlInterface):
    '''
    An instance of a Samsung brand Remote Control

    Args:
        tv (TVInterface): An instance of a class with TVInterface implements.
    '''
    tv: TVInterface
    brand = Brand.SAMSUNG

    def __post_init__(self):
        '''Validates the instance inicialization.'''
        self.validate()

    def __str__(self):
        '''Returns the representation of the object as a string.'''
        return f"{self.brand.name}"

    def toggle_power(self):
        '''
            Changes the state of TV instance.
            If TV is enable, then disable.
            If TV is disable, then enable.
        '''
        if self.tv.is_enable():
            return self.tv.disable()
        else:
            return self.tv.enable()

    def validate(self):
        '''Validation method using brands of Remote control and TV.'''
        if self.brand != self.tv.get_brand():
            raise BrandException("Dispositivos incompatíveis.")
        return True

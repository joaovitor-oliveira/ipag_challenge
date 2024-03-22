from challenge_07.src.remote_control_interface import RemoteControlInterface
from challenge_07.src.tv_interface import TVInterface
from challenge_07.src.brand import Brand
from challenge_07.src.brand_exception import BrandException
from dataclasses import dataclass


@dataclass
class SamsungRemoteControl(RemoteControlInterface):
    '''An instance of Samsung Remote Control.'''
    tv: TVInterface
    brand = Brand.SAMSUNG

    def __post_init__(self):
        '''Validation method of instance inicialization.'''
        self.validate()

    def __str__(self):
        '''Returns the representation of object as a string.'''
        return f"{self.brand.name}"

    def toggle_power(self):
        ''''
        Change the TV status.

        If TV is enable then disable.
        If TV is disable then enable.

        Returns:
            str: Actual state of TV.
        '''
        if self.tv.is_enable():
            return self.tv.disable()
        else:
            return self.tv.enable()

    def validate(self):
        '''Validates the connection between Remote Control and TV.'''
        if self.brand != self.tv.get_brand():
            raise BrandException("Dispositivos incompatíveis.")
        return True

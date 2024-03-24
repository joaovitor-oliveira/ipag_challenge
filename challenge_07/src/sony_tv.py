from challenge_07.src.brand import Brand
from challenge_07.src.tv_interface import TVInterface


class SonyTV(TVInterface):
    def __init__(self):
        '''An instance of Sony TV.'''
        self.__enable = False
        self.__brand = Brand.SONY

    def is_enable(self):
        '''
        Returns actual state of TV.

        Returns:
            bool: The actual state of TV.
        '''
        return self.__enable

    def enable(self):
        '''
        Turn on TV.

        Returns:
            str: TV status enabled.
        '''
        self.__enable = True
        return f"TV {self.__brand.name} ligada."

    def disable(self):
        '''
        Turn off TV.

        Returns:
            str: TV status disabled.
        '''
        self.__enable = False
        return f"TV {self.__brand.name} desligada."

    def get_brand(self):
        '''Returns the brand of TV.'''
        return self.__brand

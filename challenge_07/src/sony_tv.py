from challenge_07.src.brand import Brand
from challenge_07.src.tv_interface import TVInterface


class SonyTV(TVInterface):
    def __init__(self):
        '''An instance of SONY TV.'''
        self.__enable = False
        self.__brand = Brand.SONY

    def is_enable(self):
        '''
        Returns if TV is enable or not.

        Returns:
            boolean: The state of TV.
        '''
        return self.__enable

    def enable(self):
        '''
        Enable TV.

        Returns:
            str: Message with enable state of TV.
        '''
        self.__enable = True
        return f"TV {self.__brand.name} ligada."

    def disable(self):
        '''
        Disable TV.

        Returns:
            str: Message with disable state of TV.
        '''
        self.__enable = False
        return f"TV {self.__brand.name} desligada."

    def get_brand(self):
        '''Returns the brand of TV.'''
        return self.__brand

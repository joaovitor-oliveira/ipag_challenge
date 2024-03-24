from abc import ABC, abstractmethod


class FinancingMethod(ABC):
    '''Financing method interface.'''

    @abstractmethod
    def calculate_monthly_payment(self) -> float:
        '''Must be implemented.'''
        ...

    @abstractmethod
    def calculate_total_effective_cost(self) -> float:
        '''Must be implemented.'''
        ...

    @abstractmethod
    def calculate_effective_monthly_rate(self) -> float:
        '''Must be implemented.'''
        ...

    @abstractmethod
    def calculate_total_value(self) -> float:
        '''Must be implemented.'''
        ...

from challenge_09.src.financing_method_interface import FinancingMethod


class Financing:
    def __init__(self, financing_method: FinancingMethod) -> None:
        '''
        A financing instance with a selected financing method.

        Args:
            financin_method (FinancingMethod): An instance of a class with FinancingMethod implements.
        '''
        self.__financing_method = financing_method

    def calculate_monthly_payment(self) -> float:
        '''
        Calculate the monthly payment using a selected financing method.

        Returns:
            float: The monthly payment amount.
        '''
        return self.__financing_method.calculate_monthly_payment()

    def calculate_total_effective_cost(self) -> float:
        '''
        Calculate the total effective cost using a selected financing method.

        Returns:
            float: The total effective cost amount.
        '''
        return self.__financing_method.calculate_total_effective_cost()

    def calculate_effective_monthly_rate(self) -> float:
        '''
        Calculate the effective monthly rate using a selected financing method.

        Returns:
            float: The effective monthly rate amount.
        '''
        return self.__financing_method.calculate_effective_monthly_rate()

    def calculate_total_value(self) -> float:
        '''
        Calculate the total value of financing using a selected financing method.

        Returns:
            float: The total value of financing.
        '''
        return self.__financing_method.calculate_total_value()

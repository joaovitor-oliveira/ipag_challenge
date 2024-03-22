from challenge_09.src.financing_method_interface import FinancingMethod


class PriceMethod(FinancingMethod):

    def __init__(self, pv: float, n: int, i: float) -> None:
        '''
        A instance of PRICE financing method.

        Args:
            pv (float): The total financing value.
            n (int): The number of payments.
            i (float): The nominal monthly interest rate.
        '''
        self.__pv = pv
        self.__n = n
        self.__i = i

    def calculate_monthly_payment(self) -> float:
        '''
        Calculate the monthly payment.

        Returns:
            float: The monthly payment amount.
        '''
        pv = self.__pv
        n = self.__n
        i = self.__i

        pmt = pv * (i / (1 - (1 + i)**-n))
        return pmt

    def calculate_total_effective_cost(self) -> float:
        '''
        Calculate the total effective cost.

        Returns:
            float: The total effective cost.
        '''
        pv = self.__pv
        n = self.__n
        pmt = self.calculate_monthly_payment()

        cet = pmt * n - pv
        return cet

    def calculate_effective_monthly_rate(self) -> float:
        '''
        Calculate the effective monthly rate.

        Returns:
            float: The effective monthly rate.
        '''
        i = self.__i

        im = (1 + i)**(1 / 12) - 1
        return im

    def calculate_total_value(self) -> float:
        '''
        Calculate the total value of financing

        Returns:
            float: The total value of financing.
        '''
        pv = self.__pv
        cet = self.calculate_total_effective_cost()

        self.__total_value = pv + cet
        return self.__total_value

import pytest
from challenge_09.src.price_method import PriceMethod
from challenge_09.src.financing import Financing


@pytest.mark.parametrize(
    "input,expect",
    [
        ((1000, 6, 0.9), 171.96),
        ((12000, 12, 1.1), 1072.93),
        ((80000, 48, 2.3), 2769.89)
    ]
)
def test_given_a_instance_of_price_when_call_calculate_monthly_payments_then_retuns_correct_values(input, expect):
    pv, n, i = input
    expected = expect

    price = PriceMethod(pv, n, i / 100)
    financing = Financing(price)

    monthly_payment = round(financing.calculate_monthly_payment(), 2)

    assert monthly_payment == expected


@pytest.mark.parametrize(
    "input,expect",
    [
        ((1000, 6, 0.9), 31.74),
        ((12000, 12, 1.1), 875.20),
        ((80000, 48, 2.3), 52954.80)
    ]
)
def test_given_a_instance_of_price_when_call_total_effective_cost_then_returns_correct_values(input, expect):
    pv, n, i = input
    expected = expect

    price = PriceMethod(pv, n, i / 100)
    financing = Financing(price)
    tec = round(financing.calculate_total_effective_cost(), 2)

    assert tec == expected


@pytest.mark.parametrize(
    "input,expect",
    [
        ((1000, 6, 0.9), 0.75),
        ((12000, 12, 1.1), 0.91),
        ((80000, 48, 2.3), 1.9)
    ]
)
def test_given_a_instance_of_price_when_call_effective_monthly_rate_then_returns_correct_values(input, expect):
    pv, n, i = input
    expected = expect

    price = PriceMethod(pv, n, i / 100)
    financing = Financing(price)
    tec = round(financing.calculate_effective_monthly_rate() * 1000, 2)

    assert tec == expected


@pytest.mark.parametrize(
    "input,expect",
    [
        ((1000, 6, 0.9), 1031.74),
        ((12000, 12, 1.1), 12875.2),
        ((80000, 48, 2.3), 132954.8)
    ]
)
def test_given_a_instance_of_price_when_call_total_value_then_returns_correct_values(input, expect):
    pv, n, i = input
    expected = expect

    price = PriceMethod(pv, n, i / 100)
    financing = Financing(price)
    tec = round(financing.calculate_total_value(), 2)

    assert tec == expected

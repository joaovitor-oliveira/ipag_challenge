import pytest
from challenge_07.src.samsung_remote_control import SamsungRemoteControl
from challenge_07.src.lg_remote_control import LGRemoteControl
from challenge_07.src.lg_tv import LGTV
from challenge_07.src.samsung_tv import SamsungTV
from challenge_07.src.brand import Brand
from challenge_07.src.brand_exception import BrandException


@pytest.fixture
def lg_tv():
    return LGTV()


@pytest.fixture
def samsung_tv():
    return SamsungTV()


def test_given_a_correct_tv_when_call_remote_control_then_success(samsung_tv):
    tv = samsung_tv
    control = SamsungRemoteControl(tv)

    assert control.validate()


def test_given_a_correct_tv_when_call_remote_control_then_has_error(samsung_tv, capsys):

    with pytest.raises(BrandException):
        tv = samsung_tv
        control = LGRemoteControl(tv)
        control.toggle_power()


def test_when_call_str_method_then_return_brand_name(samsung_tv):
    tv = samsung_tv
    control = SamsungRemoteControl(tv)

    assert str(control) == str(Brand.SAMSUNG.name)


def test_givan_a_valid_tv_when_call_toggle_power_two_times_then_tv_enable_and_disable():
    tv = SamsungTV()
    control = SamsungRemoteControl(tv)

    expected_enable = control.toggle_power()
    expected_disable = control.toggle_power()

    assert expected_enable in f"TV {Brand.SAMSUNG.name} ligada."
    assert expected_disable in f"TV {Brand.SAMSUNG.name} desligada."

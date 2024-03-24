import pytest
from challenge_07.src.samsung_remote_control import SamsungRemoteControl
from challenge_07.src.sony_remote_control import SonyRemoteControl
from challenge_07.src.sony_tv import SonyTV
from challenge_07.src.samsung_tv import SamsungTV
from challenge_07.src.brand import Brand
from challenge_07.src.brand_exception import BrandException


@pytest.fixture
def sony_tv():
    return SonyTV()


@pytest.fixture
def samsung_tv():
    return SamsungTV()


def test_given_a_correct_tv_when_call_remote_control_then_success(sony_tv):
    tv = sony_tv
    control = SonyRemoteControl(tv)

    assert control.validate()


def test_given_a_correct_tv_when_call_remote_control_then_has_error(sony_tv, capsys):

    with pytest.raises(BrandException):
        tv = sony_tv
        control = SamsungRemoteControl(tv)
        control.toggle_power()


def test_when_call_str_method_then_return_brand_name(sony_tv):
    tv = sony_tv
    control = SonyRemoteControl(tv)

    assert str(control) == str(Brand.SONY.name)


def test_givan_a_valid_tv_when_call_toggle_power_two_times_then_tv_enable_and_disable():
    tv = SonyTV()
    control = SonyRemoteControl(tv)

    expected_enable = control.toggle_power()
    expected_disable = control.toggle_power()

    assert expected_enable in f"TV {Brand.SONY.name} ligada."
    assert expected_disable in f"TV {Brand.SONY.name} desligada."

from challenge_07.src.brand import Brand
from challenge_07.src.lg_tv import LGTV


def test_when_call_constructor_then_instantiate_a_tv():
    tv = LGTV()

    assert tv.is_enable() is False
    assert tv.get_brand() == Brand.LG


def test_givan_a_tv_when_call_enable_then_tv_is_enabled():
    tv = LGTV()

    tv.enable()

    assert tv.is_enable() is True


def test_givan_a_tv_when_call_disable_then_tv_is_disabled():
    tv = LGTV()

    tv.enable()
    tv.disable()

    assert tv.is_enable() is False

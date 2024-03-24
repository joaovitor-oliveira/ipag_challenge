from challenge_07.src.brand import Brand
from challenge_07.src.sony_tv import SonyTV


def test_when_call_constructor_then_instantiate_a_tv():
    tv = SonyTV()

    assert tv.is_enable() is False
    assert tv.get_brand() == Brand.SONY


def test_givan_a_tv_when_call_enable_then_tv_is_enabled():
    tv = SonyTV()

    tv.enable()

    assert tv.is_enable() is True


def test_givan_a_tv_when_call_disable_then_tv_is_disabled():
    tv = SonyTV()

    tv.enable()
    tv.disable()

    assert tv.is_enable() is False

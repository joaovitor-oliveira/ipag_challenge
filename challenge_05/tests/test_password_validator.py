import pytest
from challenge_05.src.password_validator import PasswordValidator


@pytest.mark.parametrize(
    "input",
    [
        "Abcdef123",
        "PASsWD09",
        "FHUFHDUIASF-H423843289423842fndafd-bcx7bytrwton"
    ]
)
def test_given_a_valid_password_when_calls_validate_then_has_no_errors(input):
    validator = PasswordValidator()

    validator.validate(input)

    assert validator.has_errors() is False


@pytest.mark.parametrize(
    "input",
    [
        "Abc123",
        "pASs09",
        "FHUFe0",
        ""
    ]
)
def test_given_a_short_password_when_calls_validate_then_has_error(input):
    validator = PasswordValidator()

    validator.validate(input)

    assert validator.has_errors() is True
    assert "A senha deve ter no mínimo 8 caracteres." in validator.get_errors()


@pytest.mark.parametrize(
    "input",
    [
        "abcqwerty1",
        "password2",
        "santosnasemi1",
    ]
)
def test_given_a_no_upper_letter_password_when_calls_validate_then_has_error(input):
    validator = PasswordValidator()

    validator.validate(input)

    assert validator.has_errors() is True
    assert "A senha deve ter pelo menos uma letra maiúscula." in validator.get_errors()


@pytest.mark.parametrize(
    "input",
    [
        "ABCQWERTY1",
        "PASSWORD2",
        "SANTOSNASEMI1",
    ]
)
def test_given_a_no_lower_letter_password_when_calls_validate_then_has_error(input):
    validator = PasswordValidator()

    validator.validate(input)

    assert validator.has_errors() is True
    assert "A senha deve ter pelo menos uma letra minúscula." in validator.get_errors()


@pytest.mark.parametrize(
    "input",
    [
        "ABCQWERTY!",
        "PASSWORD@",
        "SANTOSNASEMI#",
    ]
)
def test_given_a_no_digit_password_when_calls_validate_then_has_error(input):
    validator = PasswordValidator()

    validator.validate(input)

    assert validator.has_errors() is True
    assert "A senha deve ter pelo menos um número." in validator.get_errors()

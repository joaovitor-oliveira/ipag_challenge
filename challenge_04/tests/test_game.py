import pytest
from challenge_04.src.main import game
import challenge_04.src.main as main


MOCK_INPUT = ['50', '25', '35', 'w', '39']
MOCK_TARGET = 38


@pytest.fixture
def mock(mocker):
    mocker.patch.object(main.secrets, "randbelow", return_value=MOCK_TARGET)
    mocker.patch("builtins.input", side_effect=MOCK_INPUT)


def test_game(capsys, mock):

    game()

    out, err = capsys.readouterr()

    assert out.count("Errou!") == 3
    assert "Número inválido, tente novamente." in out
    assert "Parabéns! Você acertou em 4 tentativas." in out

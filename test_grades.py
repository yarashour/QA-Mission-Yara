import pytest

from grades import is_pass, result


@pytest.mark.parametrize(
    "score, expected",
    [
        (90, True),
        (70, True),
        (20, False),
    ],
)
def test_is_pass(score: int, expected: bool) -> None:
    assert is_pass(score) == expected


def test_result_pass() -> None:
    assert result(90) == "Pass"

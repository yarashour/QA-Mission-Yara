import pytest

from absence import can_sit_exam, status


@pytest.mark.parametrize(
    "absences, expected",
    [
        (0, True),
        (5, True),
        (9, False),
    ],
)
def test_can_sit_exam(absences: int, expected: bool) -> None:
    assert can_sit_exam(absences) == expected


@pytest.mark.parametrize(
    "absences, expected",
    [
        (0, "Allowed"),
        (3, "Allowed"),
    ],
)
def test_status(absences: int, expected: str) -> None:
    assert status(absences) == expected

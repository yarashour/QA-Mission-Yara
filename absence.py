MAX_ABSENCES = 5


def can_sit_exam(absences: int) -> bool:
    return absences <= MAX_ABSENCES


def status(absences: int) -> str:
    if can_sit_exam(absences):
        return "Allowed"
    return "blocked"

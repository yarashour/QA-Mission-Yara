PASS_MARK = 50


def is_pass(score: int) -> bool:
    return score >= PASS_MARK


def result(score: int) -> str:
    if is_pass(score):
        return "Pass"
    return "Fail"

from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_version():
    assert __version__ == '0.1.0'


def test_true_one():  # 1
    actual = multi_bracket_validation('{}')
    exbected = True
    assert actual == exbected


def test_true_two():
    actual = multi_bracket_validation('{}(){}')
    exbected = True
    assert actual == exbected


def test_true_three():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    exbected = True
    assert actual == exbected


def test_true_four():
    actual = multi_bracket_validation('(){}[[]]')
    exbected = True
    assert actual == exbected


def test_true_five():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    exbected = True
    assert actual == exbected


def test_false_one():
    actual = multi_bracket_validation('[({}]')
    exbected = False
    assert actual == exbected


def test_false_two():
    actual = multi_bracket_validation('(](')
    exbected = False
    assert actual == exbected


def test_false_three():
    actual = multi_bracket_validation('{(})')
    exbected = False
    assert actual == exbected

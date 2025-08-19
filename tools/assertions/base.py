from typing import Any, Sized


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected,(
        f"Некорректный статус-код. "
        f"Фактический статус-код: {actual}."
        f"Ожидаемый статус-код: {expected}"
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected,(
        f"Некорректное значение {name}. "
        f"Фактическое значение: {actual}."
        f"Ожидаемое значение: {expected}"
    )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (f"Некорректное значение {name}. "
                    f"Ожидается значение true, однако получено значение: {actual}")


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f"Некорректная длина объекта {name}. "
        f"Фактическая длина объекта: {len(actual)}."
        f"Ожидаемая длина объекта: {len(expected)}"
    )

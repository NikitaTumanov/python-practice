import re

import pytest as pytest


class Program:
    def __init__(self, func):
        self.func = func

    def invoke(self, param):
        return self.func(param)


@pytest.fixture
def program_2():
    p = Program(p2)
    return p


@pytest.mark.parametrize('prop,res', [
    (',?qwErT123', True),
    ('qwer,15', False),
    ('Qwer,15', True),
    ('Qw1?', False),
    ('123', False),
    ('', False)
])
def test_p2(program_2, prop, res):
    assert program_2.invoke(prop) is res


def p2(password: str) -> bool:
    """
    Программа для тестирования 2.
    Функция проверки пароля на безопасность (например: безопасный пароль
    содержит комбинирование шести или больше строчных и прописных букв,
    плюс знаки препинания и цифры).
    """
    return bool(re.match(
        r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[.,;!?]).{6,}$',
        password))
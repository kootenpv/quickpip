""" Our tests are defined in here """
from quickpip.quickpip import run


def test_run():
    TEST_NUMBER = 21
    assert run(TEST_NUMBER) == 42

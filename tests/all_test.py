from quickpip import run


def test_predict():
    TEST_NUMBER = 21
    assert run(TEST_NUMBER) == 42

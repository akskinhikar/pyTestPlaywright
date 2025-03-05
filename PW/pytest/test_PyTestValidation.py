import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I am in Pre Work")
    return "pass"

def test_initialCheck(preWork):
    print("this is first test ")
    assert preWork == "pass"

def test_initialCheck3(preSetupWork):
    print("this is first test three ")

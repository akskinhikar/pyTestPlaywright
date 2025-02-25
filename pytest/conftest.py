import pytest


@pytest.fixture(scope="session")


def preSetupWork():
    print("I am in Pre Setup Work")
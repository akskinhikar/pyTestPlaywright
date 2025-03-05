import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("I am in Pre Setup Work")

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param
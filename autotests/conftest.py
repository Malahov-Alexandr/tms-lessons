import pytest
import random


@pytest.fixture
def age():
    return random.randint(0, 100)


@pytest.fixture
def random_number_before_test(age):
    print(f" Random age is {age}")
    yield


@pytest.fixture
def delete_random_number():
    yield
    print('Deleting random age... Done')


# grouped the fixtures
@pytest.fixture
def main_fixture(random_number_before_test, delete_random_number, age):
    pass

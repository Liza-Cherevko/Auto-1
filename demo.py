import pytest


@pytest.fixture()
def before_after():
    print ("Text Before")
    yield
    print("\nAfter test")

def test_demo_1():
    assert 1==1

def test_demo_2(before_after):
    assert 2==5
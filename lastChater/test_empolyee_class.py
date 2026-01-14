import pytest

from empolyee import empolyee

def test_giving_rise_amount():
	""""testing the amount given"""
	i = empolyee('imran', 55, 70_000)
	i.give_rise(2000)
	assert i.salary == 72_000

def test_default_rise():
	""""giving default rise amount"""
	i = empolyee('imran', 55, 70_000)
	i.give_rise()
	assert i.salary == 75_000

@pytest.fixture
def imran():
	i = empolyee('imran', 55, 70_000)
	return i

def test_fixture_giving_rise_amount(imran):
	imran.give_rise(2000)
	assert imran.salary == 72_000

def test_fixture_default_rise(imran):
	""""giving default rise amount"""
	imran.give_rise()
	assert imran.salary == 75_000
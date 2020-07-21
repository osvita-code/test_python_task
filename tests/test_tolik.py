from src.tolik import congratulate_salary
import pytest

def test_simple_test():
    assert congratulate_salary(message=None, name_list=None, salary=None, bonus=None) is None

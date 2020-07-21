from src.renat import salary_remind
import pytest

def test_simple_test():
    assert salary_remind(message=None, in_days=None, name_list=None) is None

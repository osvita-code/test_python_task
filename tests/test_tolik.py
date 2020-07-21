from src.tolik import congratulate_salary


def test_simple_1_test():
    assert congratulate_salary(message="Ваш доход", name_list=["Петр"], salary=10000, bonus=2000) == \
           "Ваш доход Петр 12000"


def test_2_test():
    assert congratulate_salary(message="ВАШ доход", name_list=["Петр"], salary=10000, bonus=2000) == \
           "Ваш доход Петр 12000"


def test_3_test():
    assert congratulate_salary(message="Ваш доход", name_list=["петр"], salary=10000, bonus=2000) == \
           "Ваш доход Петр 12000"


def test_4_test():
    assert congratulate_salary(message="Ваш доход", name_list=["Петр"], salary=10000, bonus=0.2) == \
           "Ваш доход Петр 12000"


def test_5_test():
    assert congratulate_salary(message="Ваш доход", name_list=["Петр", "Иван"], salary=10000, bonus=2000) == \
           ["Ваш доход Петр 12000", "Ваш доход Иван 12000"]

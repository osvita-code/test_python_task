from src.renat import salary_remind


def test_1_test():
    assert salary_remind(message="Ваша зарплата", start_day="2020-07-21", in_days=1, name_list=["Владимир"]) == \
           "Ваша зарплата, Владимир, 2020-07-22"


def test_2_test():
    assert salary_remind(message="Ваша зарплата", start_day="2020-07-21", in_days=1, name_list=["маша"]) == \
           "Ваша зарплата, Маша, 2020-07-22"


def test_3_test():
    assert salary_remind(message="Ваша зарплата", start_day="2020-07-21", in_days=1, name_list=["Олег", "Маша"]) == \
           ["Ваша зарплата, Олег, 2020-07-22", "Ваша зарплата, Маша, 2020-07-22"]


def test_4_test():
    assert salary_remind(message="Ваша зарплата", start_day="2020-07-24", in_days=1, name_list=["Владимир"]) == \
           "Ваша зарплата, Владимир, 2020-07-27"

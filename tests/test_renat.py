from src.renat import salary_remind


def test_1_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-21",
        in_days=1,
        name_list=["Владимир"]) == "Ваша зарплата, Владимир, 2020-07-22"


def test_2_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-21",
        in_days=1,
        name_list=["маша"]) == "Ваша зарплата, Маша, 2020-07-22"


def test_3_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-21",
        in_days=1,
        name_list=[
            "Олег",
            "Маша"]) == [
        "Ваша зарплата, Олег, 2020-07-22",
        "Ваша зарплата, Маша, 2020-07-22"]


def test_4_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-24",
        in_days=1,
        name_list=["Владимир"]) == "Ваша зарплата, Владимир, 2020-07-27"


def test_5_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-23",
        in_days=2,
        name_list=["Владимир"]) == "Ваша зарплата, Владимир, 2020-07-27"


def test_6_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-22",
        in_days=3,
        name_list=["Владимир"]) == "Ваша зарплата, Владимир, 2020-07-27"


def test_7_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-21",
        in_days=4,
        name_list=["Владимир"]) == "Ваша зарплата, Владимир, 2020-07-27"


def test_8_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-20",
        in_days=5,
        name_list=["Владимир"]) == "Ваша зарплата, Владимир, 2020-07-27"


def test_9_test():
    assert salary_remind(
        message="Ваша зарплата",
        start_day="2020-07-17",
        in_days=6,
        name_list=["Владимир"]) == "Ваша зарплата, Владимир, 2020-07-27"

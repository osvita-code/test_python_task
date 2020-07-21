import datetime

def salary_remind(message, start_day, in_days, name_list):
    date = datetime.datetime.strptime(start_day, "%Y-%m-%d") + datetime.timedelta(days=in_days)
    for i in name_list:
        names = i.title()
        print("\"" + message + ", " + names + ", " + date.strftime("%Y-%m-%d") + "\"")
    return

salary_remind(message="Ваша зарплата", start_day="2020-07-21", in_days=1, name_list=["маша"])
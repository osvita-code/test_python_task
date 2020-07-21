import datetime

def salary_remind(message, start_day, in_days, name_list):
    date = datetime.datetime.strptime(start_day, "%Y-%m-%d") + datetime.timedelta(days=in_days)
    names_list = []
    for i in name_list:
        names = i.title()
        names_list.append(message + ", " + names + ", " + date.strftime("%Y-%m-%d"))
    return names_list
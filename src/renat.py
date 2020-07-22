import datetime


def salary_remind(message, start_day, in_days, name_list):
    date_datetime = datetime.datetime.strptime(start_day, "%Y-%m-%d")
    date = date_datetime + datetime.timedelta(days=int(in_days))
    if date.weekday() in (5, 6):
        date += datetime.timedelta(days=2)
    elif (date_datetime.weekday() + 1 == 5):
        date += datetime.timedelta(days=2)
        if date.weekday() in (5, 6):
            date += datetime.timedelta(days=2)
    names_list = []
    if (len(name_list) == 1):
        for i in name_list:
            names = i.title()
        return message + ", " + names + ", " + date.strftime("%Y-%m-%d")
    else:
        for i in name_list:
            names = i.title()
            names_list.append(message + ", " + names +
                              ", " + date.strftime("%Y-%m-%d"))
        return names_list

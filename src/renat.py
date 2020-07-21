import datetime

def salary_remind(message, start_day, in_days, name_list):
    date = datetime.datetime.strptime(start_day, "%Y-%m-%d") + datetime.timedelta(days=in_days)
    if date.weekday() in (5,6):
        date += datetime.timedelta(days=2)
    names_list = []
    if (len(name_list) == 1):
        for i in name_list:
            names = i.title()
        return message + ", " + names + ", " + date.strftime("%Y-%m-%d")
    else:
        for i in name_list:
            names = i.title()
            names_list.append(message + ", " + names + ", " + date.strftime("%Y-%m-%d"))
        return names_list

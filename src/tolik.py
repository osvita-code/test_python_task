def congratulate_salary(message, name_list, salary, bonus):
    if type(bonus)==type(float()):
        b = bonus*salary
    else:
        b = bonus      
    d = int(salary + b)
    f = str(d)
    nl = []
    if (len(name_list) == 1):
        for i in name_list:
            names = i.title()
        return (message.capitalize() + ' ' + names + ' ' + f)
    else:
        for i in name_list:
            names = i.title()
            nl.append(message.capitalize() + ' ' + names + ' ' + f)
        return nl    

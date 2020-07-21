def congratulate_salary(message, name_list, salary, bonus):
    if type(bonus)==type(float()):
        b = bonus*salary
    else:
        b = bonus      
    for a in name_list:
        n = a.title()
        print(message.title() + ' ' + n + salary + b)
    return

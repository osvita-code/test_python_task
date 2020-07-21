def congratulate_salary(message, name_list, salary, bonus):
    if type(bonus)==type(float()):
        b = bonus*salary
    else:
        b = bonus      
    for a in name_list:
        n = a.title()
        f = str(salary + b)
    if len(name_list) > 1:
        lists = []
    else     
        return (message.capitalize() + ' ' + n + ' ' + f)
print(congratulate_salary(message="Ваш доход", name_list=["Петр", "Иван"], salary=10000, bonus=2000))

print('Начался восьмичасовой рабочий день.')
working_hours = 8
time_worked = 0
tasks_count = 0
need_go_store = False
while time_worked < working_hours:
    time_worked += 1
    print(time_worked, '-й час')
    tasks = int(input('Сколько задач решит Максим? '))
    tasks_count += tasks

    if not need_go_store == True:
        wife_call = int(input('Звонит жена. Взять трубку? '
                              '(1 - да, 0 - нет): '))
        if wife_call == 1:
            need_go_store = True


if time_worked == working_hours:
    print('Рабочий день закончился. '
              'Всего выполнено задач:', tasks_count)
if need_go_store:
    print('Нужно зайти в магазин.')
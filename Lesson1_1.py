print("ЗАДАНИЕ 1")
ExampleList = [53, 153, 4153, 400153]
for duration in ExampleList:
    # duration = int(input("Введите продолжительность времени в сек.: "))
    if 0 <= duration < 60:
        print(f'{int(duration)} сек')
    elif 60 <= duration < 3600:
        print(f'{int(duration//60)} мин {int(duration%60)} сек')
    elif 3600 <= duration < 86400:
        print(f'{int(duration//3600)} час {int(duration//60%60)} мин {int(duration%60)} сек')
    elif duration >= 86400:
        print(f'{int(duration//86400)} дн {int(duration//3600%24)} час '
              f'{int(duration//60%60)} мин {int(duration%60)} сек')
    else:
        print("Применяемое значение является отрицательным числом!")

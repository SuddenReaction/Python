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
print("\n")


print("ЗАДАНИЕ 2")
ListCubs = []
number = 7289
numbers = 0
for num in str(number):
    numbers += int(num)
print(numbers)


summ = 0
NewList = []
for num in range(1, 10):
    ListCubs.append(num ** 3)
    print(num)
    for element in ListCubs[num - 1]:
        print(element)
        """summ += element
    if summ % 7 == 0:
        NewList.append(summ)

print(NewList)"""

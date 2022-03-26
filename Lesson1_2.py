NewList = []
ListCubs = []
First_sum = 0
Second_sum = 0
for num in range(1, 11):
    ListCubs.append(num ** 3)
    summ = 0
    for element in str(ListCubs[num - 1]):
        summ += int(element)
    if summ % 7 == 0:
        First_sum += ListCubs[num - 1]
    summ = 0
    NewList.append(ListCubs[num-1] + 17)
    for element in str(NewList[num - 1]):
        summ += int(element)
    if summ % 7 == 0:
        Second_sum += NewList[num-1]
print(f'Сумма чисел, делящихся на 7 = {First_sum}')
print(f'Сумма чисел, делящихся на 7 с учетом +17 = {Second_sum}\n\n')

# Тоже самое только без использования дополнительного списка

ListCubs.clear()  # Очистить первый список
First_sum = 0
Second_sum = 0
for num in range(1, 11):
    ListCubs.append(num ** 3)
    summ = 0
    for element in str(ListCubs[num - 1]):
        summ += int(element)
    if summ % 7 == 0:
        First_sum += ListCubs[num - 1]
    summ = 0
    for element in str(ListCubs[num-1] + 17):
        summ += int(element)
    if summ % 7 == 0:
        Second_sum += ListCubs[num - 1] + 17
print(f'Сумма чисел, делящихся на 7 = {First_sum}')
print(f'Сумма чисел, делящихся на 7 с учетом +17 = {Second_sum}')

for element in range(1, 101):
    number = str(element)
    if (int(number[0]) == 1 and len(number) == 1) or (len(number) > 1 and int(number[1]) == 1):
        print(f'{element} процент')
    elif 0 < int(number[0]) < 5 and len(number) > 1 and int(number[0]) == 1:
        print(f'{element} процентов')
    elif (len(number) == 1 and 1 < int(number[0]) < 5) or (len(number) > 1 and 1 < int(number[1]) < 5):
        print(f'{element} процентa')
    else:
        print(f'{element} процентов')

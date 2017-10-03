print 'ЗАДАНИЕ 1'
print 'Преобразователь. Программа принимает в качестве входного параметра четырехзначное число. Затем преобразует его в новое число по правилам: складывается первая и вторая, а также третья и четвертая цифры исходного числа.Полученные два числа записываются друг за другом в порядке убывания'
print 'Пример: 3165 -> 3+1=4, 6+5=11 -> ответ 114'
print 'Задание: Найти наименьшее число, в результате обработки которого автомат выдаст 1311'

def Finding_two_min_items(num):
    one = 1
    two = 0
    sum = one + two
    while sum < int(num):
        if two == 9:
            one += 1
            two = 0
        else:
            two += 1
        sum = one + two
    return str(one)+str(two)


# print Finding_two_min_items(18)


def deConverter(num):
    int_to_str = str(num)
    if len(int_to_str) == 1:
        result =  int(int_to_str+"000")
    elif len(int_to_str) == 2:
        first_part, second_part = int_to_str[1], int_to_str[0]
        result = int(Finding_two_min_items(first_part) + Finding_two_min_items(second_part))
    elif len(int_to_str) == 3:
        first_part, second_part = int_to_str[2], int_to_str[:2]
        first_part_1, second_part_1 = int_to_str[1:], int_to_str[0]
        result =  min(int(Finding_two_min_items(first_part) + Finding_two_min_items(second_part)),int(Finding_two_min_items(first_part_1) + Finding_two_min_items(second_part_1)))

    elif len(int_to_str) == 4:
        first_part, second_part = int_to_str[2:], int_to_str[:2]
        result = int(Finding_two_min_items(first_part) + Finding_two_min_items(second_part))
    if len(str(result)) > 4:
        return "wrong input!"
    else:
        return result

print deConverter(1311)
print deConverter(9)
print deConverter(13)
print deConverter(313)
print deConverter(333)

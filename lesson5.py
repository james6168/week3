#functions

# def get_sum():
#     print(2 + 4)
#
# get_sum()

# def get_circle_square():
#     r = 16
#     s = 3.14 * r**2
#     return s, r
#
# square, r = get_circle_square()
# print(square, r)

# PERCENT = 0.1
#
# money = int(input("Введите сумму: "))
# year = int(input("Введите количество лет: "))
#
# def deposit(money: int, year: int) -> float:
#     total_profit = money * PERCENT * year + money
#     return total_profit
#
# print(deposit(year=year, money=money))

#args, #kwargs
# def get_kwargs(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs.get("name"))
#     print("Fuck you")
#
# get_kwargs(1, "Nazgul", age=35, name="Nazgul")

# Задача 1

# from datetime import datetime

# def get_time_for_execution(*args):
#     if len(args) == 1:
#         time_now = datetime.now()
#         for i in range(1, args[0]):
#             print(i)
#         time_after = datetime.now() - time_now
#         return time_after
#     elif len(args) == 2:
#         time_now = datetime.now()
#         for i in range(1, args[0], args[1]):
#             print(i)
#         time_after = datetime.now() - time_now
#         return time_after
#     elif len(args) == 0:
#         time_now = datetime.now()
#         for i in range(1, 10000):
#             print(i)
#         time_after = datetime.now() - time_now
#         return time_after
#
# print(get_time_for_execution(20, 2))

# Задача 2

# def return_some_array(*args):
#     res_list = []
#     if type(args[0]) == str:
#         for each_char in args[0]:
#             res_list.append(each_char)
#         return res_list
#     elif type(args[0]) == int:
#         for i in range(1, args[0] + 1):
#             res_list.append(i)
#         return res_list
#
# print(return_some_array(20))

# Задача 1 решение от менторов:

def date_time(*args):
    from datetime import datetime
    numbers = [i for i in range(1, 10000)]
    before_time = datetime.now()
    if args and len(args) == 1:
        numbers = [i for i in range(1, args[0])]
    elif args and len(args) == 2:
        numbers = [i for i in range(1, args[0], args[1])]
    result = datetime.now() - before_time
    return result

print(date_time())
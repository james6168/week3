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

# def date_time(*args):
#     from datetime import datetime
#     numbers = [i for i in range(1, 10000)]
#     before_time = datetime.now()
#     if args and len(args) == 1:
#         numbers = [i for i in range(1, args[0])]
#     elif args and len(args) == 2:
#         numbers = [i for i in range(1, args[0], args[1])]
#     result = datetime.now() - before_time
#     return result
#
# print(date_time())

#Командная задача №4

play_field = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


def put_symbol (some_symbol_coordinates: list):
    position_x = int(some_symbol_coordinates[0])
    position_y = int(some_symbol_coordinates[1])
    input_symbol = int(some_symbol_coordinates[2])

    if input_symbol == 2:
        if play_field[position_x][position_y] == 0:
            play_field[position_x][position_y] = "O"
        else:
            print("Данная ячейка занята")

    elif input_symbol == 1:
        if play_field[position_x][position_y] == 0:
            play_field[position_x][position_y] = "X"
        else:
            print("Данная ячейка занята")
    print(f"{play_field[0]}\n{play_field[1]}\n{play_field[2]}")


count_of_0 = 0
count_of_x = 0
count_of_y = 0

while True:
    input_player = input("Введите координаты в списке и с 2 для O или с 1 для Х в конце этого списка: ")
    put_symbol(input_player.split())

    vertical_column_1 = [play_field[0][0], play_field[1][0], play_field[2][0]]
    vertical_column_2 = [play_field[0][1], play_field[1][1], play_field[2][1]]
    vertical_column_3 = [play_field[0][2], play_field[1][2], play_field[2][2]]

    diagonal_1 = [play_field[0][0], play_field[1][1], play_field[2][2]]
    diagonal_2 = [play_field[0][2], play_field[1][1], play_field[2][0]]

    for each_array in play_field:
        if 0 not in each_array:
            count_of_0 += 1
    if count_of_0 == 3:
        break

    if play_field[0].count("X") == 3 or play_field[1].count("X") == 3 or play_field[2].count("X") == 3:
        print("Игра оконченна, X победил")
        break
    elif play_field[0].count("O") == 3 or play_field[1].count("O") == 3 or play_field[2].count("O") == 3:
        print("Игра оконченна, O победил")
        break
    elif vertical_column_1.count("X") == 3 or vertical_column_2.count("X") == 3 or vertical_column_3.count("X") == 3:
        print("Игра оконченна, X победил")
        break
    elif vertical_column_1.count("O") == 3 or vertical_column_2.count("O") == 3 or vertical_column_3.count("O") == 3:
        print("Игра оконченна, O победил")
        break
    elif diagonal_1.count("X") == 3 or diagonal_2.count("X") == 3:
        print("Игра оконченна, X победил")
        break
    elif diagonal_1.count("O") == 3 or diagonal_2.count("O") == 3:
        print("Игра оконченна, O победил")
        break






















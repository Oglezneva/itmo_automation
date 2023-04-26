# # ЗАДАЧА 1

# def task(a: int, b: int):
#     return max(a, b)
#
#
# #print(task(5, 9))
#
#
# def task2(a: int, b: int):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
#
# task2(input(), input())

# ЗАДАЧА 2

# def task(a: int, b: int):
#      if a - b == 135 or b - a == 135:
#          print('Yes')
#      else:
#          print('No')
#
# task(300, 435)

# ЗАДАЧА 3


def season(x):
    match x:
        case 12 | 1 | 2:
            print('Зима')
        case 3 | 4 | 5:
            print('Весна')
        case 6 | 7 | 8:
            print('Лето')
        case 9 | 10 | 11:
            print('Осень')


season(6)


# ЗАДАЧА 4


# def task(a, b, c):
#     if a > 10 and b > 10 and c > 10:
#         print('Yes')
#     else:
#         print('No')
#
#
# task(21, 22, 23)



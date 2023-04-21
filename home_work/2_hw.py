

def task_1() -> tuple:
    a: int = 5
    b: float = 1.12
    c: str = 'строка'
    d: list = [1, 2]
    e: bool = True

    print('type=' + str(type(a)))
    print('value=' + str(a))
    print('type=' + str(type(b)))
    print('value=' + str(b))
    print('type=' + str(type(c)))
    print('value=' + c)
    print('type=' + str(type(d)))
    print('value=' + str(d))
    print('type=' + str(type(e)))
    print('value=' + str(e))
    return a, b, c, d, e


result = task_1()
print(str(result))


def task_2_by_index() -> (int, int, int):
    list_a = [1, 2, 3, 5, 8, 13, 21] # это ряд Фибоначчи
    print('first = ' + str(list_a[0]))
    print('second = ' + str(list_a[1]))
    print('third = ' + str(list_a[2]))
    return list_a[0], list_a[1], list_a[2]


#task_2_by_index()


def task_2_by_loop():
    list_a = [1, 2, 3, 5, 8, 13, 21]

    counter = 0
    for element in list_a:
        if counter <= 2:
            print(element)
        else:
            break
        counter += 1


#task_2_by_loop()





def task_3(a: int) -> int:
    return pow(a, 2)


#print(task_3(5))


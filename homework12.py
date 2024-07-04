n = int(input('Введите число: '))
def code(x):
    #rt = [] # создание пар суммы кратных чисел
    for i in range(1, x + 1):
        if i >= x / 2:
            break
        for j in range(2, x + 1):
            sum_ = i +j
            if x % sum_ == 0:
                print(f'{i}{j}', end="")
list_code = code(n)
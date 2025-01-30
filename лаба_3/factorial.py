def factorial(x):
    """
    если факториала нет, то функция выдает код 0,
    если факториал есть, то возвращает его
    """
    # if not isinstance(x, int):
    #     raise ValueError
    if x < 0:
        raise ValueError
    fact = 1
    for i in range(2, x + 1):
        fact *= i
    return fact

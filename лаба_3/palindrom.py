def is_palindrom(s):
    """
    функция возвращает True, если строка является палиндромом,
    если строка не является палиндромом, то она возвращает False
    (регистр не учитывается)
    """
    s = s.lower()
    if len(s) < 3:
        raise ValueError
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

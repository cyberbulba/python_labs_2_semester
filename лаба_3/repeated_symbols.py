def repeated_symbols(s):
    """
    функция возвращает количество символов, которые встречаются в строке
    больше 1 раза (с учётом регистра)
    """
    if s == '':
        raise ValueError
    symbs = {symb: s.count(symb) for symb in set(s)}
    repeated_symbs = list(filter(lambda symb: symbs[symb] > 1, symbs))
    return len(repeated_symbs)

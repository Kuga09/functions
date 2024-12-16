def combinations(lst):
    # Базовый случай: если список пуст, вернуть список с пустым сочетанием
    if not lst:
        return [[]]

    # Рекурсивно получаем сочетания для оставшейся части списка
    rest_combinations = combinations(lst[1:])

    # Добавляем к каждому сочетанию текущий элемент и объединяем
    return rest_combinations + [[lst[0]] + comb for comb in rest_combinations]

# Пример использования
lst = [1, 2, 3, 4]
result = combinations(lst)
print(result)

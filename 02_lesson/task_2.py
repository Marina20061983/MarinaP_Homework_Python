# Определяем функцию
def is_year_leap(year):
    # Проверяем, делится ли год на 4
    if year % 4 == 0:
        return True
    else:
        return False


# Выберите любой год для проверки, например, 2020
year_to_check = 2020

# Вызываем функцию и сохраняем результат в переменную
is_leap = is_year_leap(year_to_check)

# Выводим результат в консоль
print(f'год {year_to_check}: {is_leap}')

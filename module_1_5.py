# 2 Задайте переменные разных типов данных:
#  - Создайте переменную immutable_var и присвойте ей кортеж
#   из нескольких элементов разных типов данных.
#  - Выполните операции вывода кортежа immutable_var на экран.
immutable_var = (["Оля","Вадим"], 33, 145, True)
print(immutable_var)
print(type(immutable_var))
# 3 Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var.
#   Объясните, почему нельзя изменить значения элементов кортежа.
# immutable_var[2] = 66
print(immutable_var)
print(type(immutable_var))
#  попытка изменить элемент кортежа, например 33 на 66: immutable_var[2] = 66
#  выдаст ошибку, т.к кортеж не поддерживает обращение по элементам.

# 4. Создание изменяемых структур данных:
# - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# - Измените элементы списка mutable_list. Выведите на экран измененный список mutable_list.
mutable_list=[11,22,33,44]
print(mutable_list)
print(type(mutable_list))
# Добавляем новый элемент в список 88
mutable_list.append(88)
print(mutable_list)
print(type(mutable_list))
# Заменяем элемент в списке с 44 на 100 элемент
mutable_list[3]=100
print(mutable_list)
print(type(mutable_list))

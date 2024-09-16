def get_matrix(n, m, value):
#Создаем пустой список для хранения матрицы
    matrix = []
#Внешний цикл для создания строк
    for i in range(n):
#Добавляем пустой список для новой строки
        row = []
#Внутренний цикл для заполнения строки
        for j in range(m):
#Добавляем значение в строку
            row.append(value)
# Добавляем заполненную строку в матрицу
        matrix.append(row)
#Возвращаем матрицу
    return matrix
#Пример использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

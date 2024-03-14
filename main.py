import os
def levenshtein_distance(s1, s2):
    """
    Вычисляет расстояние Левенштейна между двумя строками.
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def find_partial_matches(s1, s2):
    """
    Находит частичные соответствия строк из s1 строкам из s2
    с оценкой различия по расстоянию Левенштейна                !!!(distance <= 2)!!!
    """
    matches = []
    for str1 in s1:
        for str2 in s2:
            distance = levenshtein_distance(str1, str2)
            if distance <= 2:
                matches.append({'s1': str1, 's2': str2, 'distance': distance})
    return matches


if __name__ == '__main__':
    # путь к директории виртуального окружения
    venv_dir = os.path.dirname(os.path.abspath(__file__))

    # Пути к файлам
    file1_path = os.path.join(venv_dir, 's1_list.txt')
    file2_path = os.path.join(venv_dir, 's2_list.txt')
    result_file_path = os.path.join(venv_dir, 'result.txt')

    # Чтение файлов
    with open(file1_path, 'r') as file:
        s1 = file.readlines()

    with open(file2_path, 'r') as file:
        s2 = file.read().split()  # Разбиваем длинную строку на отдельные


    # Удаление символов новой строки из строк
    s1 = [line.strip() for line in s1]

    # Запуск основной фунции
    result = find_partial_matches(s1, s2)
    # Запись результата в файл резалт.тхт
    with open(result_file_path, 'w') as result_file:
        for item in result:
            result_file.write(f"s1: {item['s1']}, s2: {item['s2']}, distance: {item['distance']}\n")


def find_first_duplicate_pair(sentence):
    """Находит первую пару одинаковых соседних символов и выводит их индексы."""
    for i in range(len(sentence) - 1):
        if sentence[i] == sentence[i + 1]:
            print(f"Первая пара одинаковых соседних символов: '{sentence[i]}' на позициях {i} и {i + 1}.")
            return
    print("Пары одинаковых соседних символов не найдено.")

# Ввод данных
sentence = input("Введите предложение: ")

# Поиск и вывод результата
find_first_duplicate_pair(sentence)
def remove_odd_o(sentence):
    """Удаляет буквы 'о' с нечетных позиций в строке."""
    result = []
    for index, char in enumerate(sentence):
        # Проверяем, является ли индекс нечетным и символ 'о'
        if not (index % 2 == 1 and char.lower() == 'о'):
            result.append(char)
    return ''.join(result)

# Ввод данных
sentence = input("Введите предложение: ")

# Удаление букв 'о' с нечетных позиций и вывод результата
modified_sentence = remove_odd_o(sentence)
print("Измененное предложение:", modified_sentence)

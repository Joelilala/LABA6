def print_character_occurrences(sentence, character):
    """Выводит все вхождения заданного символа в предложении столбиком."""
    occurrences = [index for index, char in enumerate(sentence) if char == character]
    
    if occurrences:
        print(f"Символ '{character}' встречается на позициях:")
        for index in occurrences:
            print(index)
    else:
        print(f"Символ '{character}' не найден в предложении.")

# Ввод данных
sentence = input("Введите предложение: ")
character = input("Введите символ для поиска: ")

# Проверка на ввод одного символа
if len(character) != 1:
    print("Пожалуйста, введите только один символ.")
else:
    print_character_occurrences(sentence, character)

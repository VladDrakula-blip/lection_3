# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
def remove_digits(text):
    # Удаление цифр из текста
    return ''.join([char for char in text if not char.isdigit()])

# Открытие исходного файла для чтения
with open("test_file/task1_data.txt", 'r', encoding='utf-8') as file:
    # Чтение содержимого файла
    text = file.read()

# Удаление цифр из текста
cleaned_text = remove_digits(text)

# Открытие файла для записи
with open("test_file/task1_answer.txt", 'w', encoding='utf-8') as file:
    # Запись очищенного текста в файл
    file.write(cleaned_text)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')

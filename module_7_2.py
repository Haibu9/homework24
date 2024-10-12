from pprint import pprint
import io

def custom_write(file_name, strings):
    file_name = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    num = 1
    for str_ in strings:
        key = (num, file_name.tell())
        strings_positions[key] = str_
        num += 1
        file_name.write(f'{str_}\n')

    file_name.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


# Чтение исходной строки из файла
with open('input.txt', 'r') as file:
  input_string = file.read().strip()

# Проверка длины строки
if len(input_string) == 1:
  result_string = input_string
else:
# Разделение строки на пирамиды по 4 символа
  pyramid_list = [input_string[i:i+4] for i in range(0, len(input_string), 4)]

# Сжатие пирамид
while True:
  new_pyramid_list = []
  for pyramid in pyramid_list:
    if len(set(pyramid)) == 1:
      new_pyramid_list.append(pyramid[0])
    else:
      new_pyramid_list.append(pyramid)

# Формирование результирующей строки
result_string = ''.join(pyramid_list)

# Запись результирующей строки в файл
with open('output.txt', 'w') as file:
  file.write(result_string)
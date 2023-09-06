text = input("Введите текст: ")


max_count = 0
current_count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        current_count += 1
    else:
        current_count = 1


    if current_count > max_count:
        max_count = current_count

print("Наибольшее количество идущих подряд одинаковых символов:", max_count)

# Як перекласти слово з украінською на англійську в Python?


# pip install googletrans==4.0.0-rc1

from googletrans import Translator

translator = Translator()

# Запитуємо слово у користувача
text = input("Введіть слово украінською: ")

# Перекладаємо на англійську
result = translator.translate(text, src="uk", dest="en")

print("Переклад:", result.text)




# Домашнє завдання:

# Зробіть програму, яка:

# Запитує у користувача 2 слова (українською)

# Перекладає їх на англійську та французьку

# Виводить переклади у форматі:

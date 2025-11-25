# Як працює реверс рядка в Python?


#  Створюємо рядок
text = "PythonIsFun"

# Реверс рядка (перевертаємо його задом наперед)
reversed_text = text[::-1]
print("Перевернутий рядок:", reversed_text)
# text[start:stop:step] → step=-1 дає реверс

# Беремо кожну другу літеру
every_second = text[::-2]
print("Кожна друга літера реверсом:", every_second)
# тут step=-2, пропускаємо один символ

# Перші 5 символів реверсу
first_five = reversed_text[:5]
print("Перші 5 символів:", first_five)
#  slicing від 0 до 5, включає індекси 0..4


# Домашка
# Слово "DataScienceIsAwesome" 
# Створи свій власний реверс, виведи кожну третю літеру
# напиши в коментарях що саме робить твій slice





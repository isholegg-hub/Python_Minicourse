# Вставка даних до таблиці в базу даних  на Python
# продовження роботи з базами на Python


import sqlite3

# 1. Підключення до тієї ж бази
conn = sqlite3.connect('my_first_db.db')
c = conn.cursor()

# 2. Вставка кількох рядків у таблицю
c.execute("INSERT INTO users VALUES (7, 'Anna')")
c.execute("INSERT INTO users VALUES (8, 'Bohdan')")

# Зберігаємо зміни
conn.commit()

# 3. Вибірка всіх рядків із таблиці
c.execute("SELECT * FROM users")
rows = c.fetchall()

print("Список користувачів у таблиці users:")
for row in rows:
    print(row)

# 4. Закриття підключення
conn.close()


# Домашнє завдання:
# Вставте свої дані

# Додайте ще 2–3 рядки у таблицю users з іншими іменами.

# Спробуйте змінити id або name для деяких рядків.

# Спробуйте зробити вибірку

# Наприклад, вибрати користувача за конкретним id через SELECT * FROM users WHERE id=….
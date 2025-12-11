# Підключаємося до MySQL

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="StudyProject",
    port=8889  # обов'язково порт MAMP
)

cursor = db.cursor()

# ======================
# 1. Вибірка даних
# ======================
print("Вибірка всіх користувачів:")
cursor.execute("SELECT * FROM users")

result = cursor.fetchall()

for row in result:
    print(row)

# ======================
# 2. Додавання нового користувача
# ======================
cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
               ("Dasha", "dasha@example.com", "3434343434"))
db.commit()
print("Користувача додано!")

# Перевіримо ще раз таблицю
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print("Тепер таблиця виглядає так:")
for row in result:
    print(row)

db.close()


# # Домашнє завдання:

# Додати ще одного користувача на свій вибір

# Зробити вибірку тільки по імені та віку (SELECT name, age FROM users)

# Написати в коментарях, кого ви додали і що отримали в результаті



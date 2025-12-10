

import sqlite3

conn = sqlite3.connect('my_first_db.db')
c = conn.cursor()

# Видаляємо рядок з id = 1
c.execute("DELETE FROM users WHERE id = 2")

conn.commit()

# Перевіряємо, що залишилось
c.execute("SELECT * FROM users")
print(c.fetchall())

conn.close()


# # Домашнє завдання:
# Видалити будь-який інший запис (наприклад, WHERE name='Ivan').

# Перевірити, що залишилось у таблиці.

# Написати у коментарях, який саме запис ви видалили.
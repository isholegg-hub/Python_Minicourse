

import sqlite3

# Підключаємося до бази
conn = sqlite3.connect('my_first_db.db')
c = conn.cursor()

# Оновлюємо користувача з id = 5
c.execute("UPDATE users SET name = 'Jack' WHERE id = 6")

conn.commit()

# Перевіряємо, що змінилось
c.execute("SELECT * FROM users")
print(c.fetchall())

conn.close()

# # Домашнє завдання:
# 1. Оновіть вік будь-якого іншого користувача (наприклад, WHERE name='Ivan').
# 2. Спробуйте змінити ще одне поле (наприклад, name='Petro').
# 3. Перевірте таблицю, що змінились саме ті записи.
# 4. Напишіть у коментарях, які записи ви оновили.

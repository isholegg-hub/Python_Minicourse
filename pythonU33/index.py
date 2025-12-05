# Авто-резервне копіювання папок у поточній директорії проекту на Python?


import os
import shutil
from datetime import datetime

# Поточна папка проекту (де запускається скрипт)
current_folder = os.getcwd()

# Папка для резервування (відносно поточної)
source_folder = os.path.join(current_folder, "Important")

# Папка для збереження резервних копій
backup_root = os.path.join(current_folder, "Backups")

# Переконуємось, що папка для бекапів існує
os.makedirs(backup_root, exist_ok=True)

# Перевіряємо, чи існує папка Important
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print(f"Папка '{source_folder}' створена для прикладу. Додайте туди файли для резервного копіювання.")
else:
    # Створюємо унікальну назву для резервної копії за датою та часом
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(backup_root, f"backup_{now}")

    # Копіюємо всю папку разом з файлами та підпапками
    shutil.copytree(source_folder, os.path.join(backup_folder, os.path.basename(source_folder)))

    print(f"Резервна копія створена: {backup_folder}")





# # Домашнє завдання:
# Розширення резервного копіювання

# Модифікуйте скрипт так, щоб він створював резервну копію не однієї, а кількох папок одночасно.

# Наприклад: Important, Projects, Docs → копіюються всі в одну папку бекапів.

# У коментарях напишіть: “Резервне копіювання працює/не працює.”
# Хто напише коментар - отримає додаткове бонусне завдання!
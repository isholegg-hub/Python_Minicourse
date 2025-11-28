# Перевірка наявності інтернету у скрипті Python?



import socket

def check_internet(host="8.8.8.4", port=53, timeout=3):
    """
    Перевіряє, чи є підключення до інтернету
    host: DNS-сервер Google
    port: порт
    """
    try:
          # Встановлюємо таймаут для підключення (чекаємо не більше `timeout` секунд)
        socket.setdefaulttimeout(timeout)
          # Створюємо новий сокет для IPv4 (AF_INET) та TCP (SOCK_STREAM)
    # і намагаємося підключитися до хоста і порту
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as e:
        return False

if check_internet():
    print("Інтернет підключений ")
else:
    print("Немає підключення до інтернету ")



# Домашнє завдання:

# Змініть функцію, щоб вона перевіряла підключення до будь-якого іншого хосту 
# (наприклад, ваш сайт або сервер).

# У коментарях напишіть: “Перевірка підключення працює/не працює.”
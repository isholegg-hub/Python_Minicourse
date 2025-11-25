# Як  почистити "брудні" рядки на Python швидко?



# 1) Маємо "брудні" дані
raw_name = "   oLyA   "
raw_city = "KyiV!!!"
raw_email = "   USER@MAIL.COM  "

print("Оригінал:", raw_name, raw_city, raw_email)


# 2) strip() — прибираємо зайві пробіли
clean_name = raw_name.strip()

# 3) lower() — робимо однаковий регістр
clean_email = raw_email.strip().lower()

# 4) replace() — забираємо зайві символи
clean_city = raw_city.replace("!", "")

# 5) Результат
print("Очищено:", clean_name, clean_city, clean_email)



# Домашка
# text = "   ПрИвІт, МеНе ЗвУтИ JOhN!!!   "
# Почистити текст так, щоб було: "Привіт, мене звути John"

# Як порахувати слова у TXT та PDF файлах python?




import PyPDF2
# pip install PyPDF2

# функція для підрахунку слів у TXT-файлі
def count_words_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()
        return len(words)

# функція для підрахунку слів у PDF-файлі
def count_words_pdf(path):
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        words = text.split()
        return len(words)

# тестові файли у тій самій папці
txt_path = "sample_text.txt"
pdf_path = "sample_pdf.pdf"

print("TXT:", count_words_txt(txt_path), "слів ")
print("PDF:", count_words_pdf(pdf_path), "слів ")




# Домашнє завдання (UA)

# Додай підрахунок символів окремо від слів.

# Додай підрахунок унікальних слів (через set).

# Зроби, щоб можна було рахувати кілька файлів одразу (список шляхів).
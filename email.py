from datetime import date
import math

# 1. Создаём словарь email

email = {
    "subject": "Важное сообщение",
    "from": "  Evgeniy@Gmail.com  ",
    "to": "  HR@company.ru  ",
    "body": "Здравствуйте!\n\tХочу пройти собеседование.\nС уважением, Евгений.",
}

# 2. Добавляем дату отправки в формате YYYY-MM-DD

send_date = date.today().isoformat()
email["date"] = send_date

# 3. Нормализуем e-mail: убираем пробелы и приводим к нижнему регистру

email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. Извлекаем логин и домен отправителя

sender = email["from"]
login, domain = sender.split("@")  # разделяем по символу '@'

# 5. Создаём сокращённую версию текста

short_body = email["body"][:10] + "..."
email["short_body"] = short_body

# 6. Списки доменов (только уникальные значения — используем set)

personal_domains = list(
    {
        "gmail.com",
        "list.ru",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "icloud.com",
        "yandex.ru",
        "mail.ru",
        "bk.ru",
        "inbox.ru",
    }
)

corporate_domains = list(
    {
        "company.ru",
        "corporation.com",
        "university.edu",
        "organization.org",
        "business.net",
    }
)

# 7. Проверка: нет ли пересечений между личными и корпоративными доменами

intersection = set(personal_domains) & set(corporate_domains)
assert len(intersection) == 0, f"Общие домены найдены: {intersection}"

# 8. Проверяем «корпоративность» отправителя

is_corporate = domain in corporate_domains

# 9. Очищаем текст от табов и переносов строк

clean_body = email["body"].replace("\t", " ").replace("\n", " ")
email["clean_body"] = clean_body

# 10. Формируем текст отправленного письма

email[
    "sent_text"
] = f"""Кому: {email['to']}, от {email['from']}
Тема: {email['subject']}, дата {email['date']}
{email['clean_body']}"""

# 11. Рассчитываем количество страниц (по 500 символов на страницу, округление вверх)

total_chars = len(email["sent_text"])
pages = math.ceil(total_chars / 500)

# 12. Проверяем пустоту темы и тела

is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

# 13. Создаём маску e-mail отправителя

masked_from = login[:2] + "***@" + domain
email["masked_from"] = masked_from

# 14. Удаляем "list.ru" и "bk.ru" из списка личных доменов

personal_domains = [d for d in personal_domains if d not in {"list.ru", "bk.ru"}]

print(email)
print(is_corporate, is_subject_empty, is_body_empty, pages)

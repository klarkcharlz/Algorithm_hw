"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
from hashlib import sha256
from uuid import uuid4
import sqlite3


# создаем БД, подключаемся к ней и создаем таблицу
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users("
          "name TEXT,"
          "salt TEXT,"
          "password TEXT);")
conn.commit()


def registration():
    """Регистрация новых пользователей."""
    print("Регистрация!")
    name = input("Пожалуйста введите Ваше имя:\n")
    # проверяем что такого пользователя еще нету в БД
    sel = c.execute("SELECT * FROM users WHERE name = ?;", (name,)).fetchall()
    if sel:
        print("Вы уже есть в базе. Регистрация не требуется")
        return
    password = input("Пожалуйста введите ваш пароль:\n")
    salt = uuid4().hex.encode('utf-8')  # создаем уникальную соль во время регистрации пользователя
    hash_password = sha256(salt + password.encode('utf-8')).hexdigest()
    passwd = input("Пожалуйста введите ваш пароль повторно:\n")
    hash_passwd = sha256(salt + passwd.encode('utf-8')).hexdigest()
    if hash_passwd == hash_password:
        print("Регистрация выполнена!")
        # сохраняем данные о пользователе
        insert_code = "INSERT INTO users VALUES (?, ?, ?);"
        c.execute(insert_code, (name, salt, hash_password))
        conn.commit()
        return
    else:
        print("Регистрация не выполнена!")  # в случае ошибочного повторно ввода пароля
        return


def autorization():
    """Авторизация зарегестрированных пользователей"""
    print("Авторизация!")
    name = input("Пожалуйста введите Ваше имя:\n")
    # ищем пользователя в БД
    sel = c.execute("SELECT name, salt, password FROM users WHERE name = ?;", (name,)).fetchall()
    if sel:
        salt = sel[0][1]
        hash_passwd = sel[0][2]
    else:
        print("Вас нету в базе данных, вам необходимо выполнить регистрацию!")
        return
    password = input("Пожалуйста введите ваш пароль:\n")
    if sha256(salt + password.encode('utf-8')).hexdigest() == hash_passwd:
        print("Доступ разрешен!")
        return
    else:
        print("доступ запрещен!")
        return


registration()
autorization()

conn.close()

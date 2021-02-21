"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from sys import argv
from hashlib import md5
import json
import os.path
from pathlib import Path


def hash_urls():
    if os.path.exists('hash.txt'):  # проверяем существует ли файл для хранения данных
        print(f"Принятый url: {argv[1]}")
        salt = argv[1].split('.')[1]  # будем использовать вот такую соль
        hashing = md5(salt.encode('utf-8') + argv[1].encode('utf-8')).hexdigest()
        with open('hash.txt', 'r') as f:
            data = f.read()
            try:
                data = json.loads(data)
            except json.decoder.JSONDecodeError:
                data = {}
            if hashing in data:
                print(f"По данному хешу содержится: {data[hashing]}")
            else:
                data[hashing] = argv[1]
            with open('hash.txt', 'w') as file:
                file.write(json.dumps(data))
    else:  # если не существует создаем его и заново вызываем функцию
        Path('hash.txt').touch()
        hash_urls()


hash_urls()

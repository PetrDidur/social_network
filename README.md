Описание проекта

Этот проект представляет собой веб-приложение для создания постов и комментариев.

Технические требования

Python 3.8+
Django 3+
Django Rest Framework (DRF) 3.10+
PostgreSQL 10+
Установка

Склонируйте репозиторий:
bash
Copy code
git clone https://github.com/your/repository.git
Установите зависимости:
Copy code
pip install -r requirements.txt
Создайте и примените миграции:
Copy code
python manage.py makemigrations
python manage.py migrate
Запустите сервер:
Copy code
python manage.py runserver
Перейдите по адресу http://127.0.0.1:8000/ в вашем веб-браузере.
Эндпоинты

/api/users/ - CRUD операции для пользователей.
/api/posts/ - CRUD операции для постов.
/api/comments/ - CRUD операции для комментариев.
Валидаторы

Модель пользователя
Валидатор для пароля: должен быть не менее 8 символов и содержать хотя бы одну цифру.
Валидатор для почты: разрешены домены mail.ru и yandex.ru.
Модель поста
Проверка возраста автора поста: должен быть старше 18 лет.
Проверка заголовка на наличие запрещенных слов: ерунда, глупость, чепуха.

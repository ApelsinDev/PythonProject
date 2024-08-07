
# Сервис, который принимает и отвечает на HTTP запросы
## Автор
Журавлев Никита \
Самарский университет\
Группа: 6305-010302D

## Описание
Этот проект представляет собой веб-приложение на основе фреймворка Django, предназначенное для управления информацией о магазинах в различных городах и на различных улицах. Приложение предоставляет REST API для взаимодействия с данными о городах, улицах и магазинах.
## Задание 
Реализовать сервис, который принимает и отвечает на HTTP запросы.

### Функционал:
1. В случае успешной обработки сервис должен отвечать статусом 200, в случае любой ошибки — статус 400.

2. Сохранение всех объектов в базе данных.
3. Запросы:
- GET /city/ — получение всех городов из базы;
- GET /city/{city_id}/street/ — получение всех улиц города; (city_id — идентификатор города)
- POST /shop/ — создание магазина; Данный метод получает json с объектом магазина, в ответ возвращает id созданной записи.
- GET /shop/?street=&city=&open=0/1 — получение списка магазинов;
  - Метод принимает параметры для фильтрации. Параметры не обязательны. В случае отсутствия параметров выводятся все магазины, если хоть один параметр есть, то по нему выполняется фильтрация.
  - Важно: в объекте каждого магазина выводится название города и улицы, а не id записи.
  - Параметр open: 0 — закрыт, 1 — открыт. Данный статус определяется исходя из параметров «Время открытия», «Время закрытия» и текущего времени сервера.
### Объекты:
#### Магазин:
- Название
- Город
- Улица
- Дом
- Время открытия
- Время закрытия 
#### Город:
- Название 
#### Улица:
- Название
- Город 
##### !! Замечание: поля id у объектов не указаны, но подразумевается что они есть.

##### !! Важно: Выстроить связи между таблицами в базе данных.

### Инструменты:
- Фреймворк для обработки http запросов Django + Django Rest Framework
- Реляционная БД (выбрал PostgreSQL)
- Запросы в базу данных через ORM (ORM на выбор).
## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_пользователь/название_репозитория.git
   cd название_репозитория
   ```

2. Создайте виртуальную среду, если это ещё не сделано, и активируйте её:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Windows: .venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` в папке "myproject" и добавьте туда следующие строки:
   ```plaintext
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
   
## Настройка базы данных PostgreSQL
Если у вас еще нет базы данных, выполните следующие шаги:


1. Запустите PostgreSQL и войдите в оболочку PostgreSQL:
     ```bash
     psql -U postgres
     ```

2. Создайте базу данных и пользователя:
     ```sql
     CREATE DATABASE your_db_name;
     CREATE USER your_db_user WITH PASSWORD 'your_db_password';
     ALTER ROLE your_db_user SET client_encoding TO 'utf8';
     ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
     ALTER ROLE your_db_user SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
     ```

3. Предоставьте права на схему public:
     ```sql
     GRANT ALL PRIVILEGES ON SCHEMA public TO your_db_user;
     ALTER USER your_db_user CREATEDB;
     ```
## Применение миграций и заполнение базы данных 
1. Примените миграции:
   ```bash
   python manage.py migrate
   ```
2. Для заполнения базы данных начальными данными выполните следующую команду:
   ```bash
   python manage.py populate_data
   ```
   
## Запуск сервера
Запустите сервер:
   ```bash
   python manage.py runserver
   ```
## Проверка работоспособности
### Использование Django админки
1. Создайте суперпользователя, если уже этого не сделали:
   ```bash
   python manage.py createsuperuser
   ```
2. Перейдите в админку по адресу http://127.0.0.1:8000/admin/ и войдите под учетной записью суперпользователя.

### Использование Postman или curl для выполнения HTTP-запросов

Примеры запросов 

- Получение списка городов:
   ```http request
   GET http://127.0.0.1:8000/api/cities/
   ```
- Получение списка улиц:
   ```http request
   GET http://127.0.0.1:8000/api/streets/
   ```
- Получение списка улиц для конкретного города:
   ```http request
   GET http://127.0.0.1:8000/api/streets/?city_id=1
   ```
- Получение списка магазинов:
   ```http request
   GET http://127.0.0.1:8000/api/shops/
   ```
- Создание магазина:
   ```http request
   POST http://127.0.0.1:8000/api/shops/
   Content-Type: application/json

   {  
      "name": "Новый Магазин",
      "city": 1,
      "street": 1,
      "building": "10",
      "opening_time": "09:00:00",
      "closing_time": "21:00:00"
   }
    ```
- Фильтрация магазинов:
    ```http request
    GET http://127.0.0.1:8000/api/shops/filter_shops/?city=Москва&open=1
    ```
### Использование curl
1. Получение списка городов:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/cities/
    ```
2. Получение списка улиц:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/streets/
    ```
3. Получение списка улиц для конкретного города:
    ```bash
    curl -X GET "http://127.0.0.1:8000/api/streets/?city_id=1"
    ```
4. Получение списка магазинов:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/shops/
    ```
5. Создание магазина:
    ```bash
    curl -X POST http://127.0.0.1:8000/api/shops/ \
    -H "Content-Type: application/json" \
    -d '{"name": "Новый Магазин", "city": 1, "street": 1, "building": "10", "opening_time": "09:00:00", "closing_time": "21:00:00"}'
    ```
6. Фильтрация магазинов:
    ```bash
    curl -X GET "http://127.0.0.1:8000/api/shops/filter_shops/?city=Москва&open=1"
    ```

## Проблемы и решения

### Ошибка "нет доступа к схеме public"

Если при выполнении миграций вы получаете ошибку "нет доступа к схеме public", выполните следующие шаги:

1. Запустите PostgreSQL и войдите в оболочку PostgreSQL:
   ```bash
   psql -U postgres
   ```

2. Предоставьте все привилегии пользователю:
   ```sql
   GRANT ALL PRIVILEGES ON SCHEMA public TO your_db_user;
   ALTER USER your_db_user CREATEDB;
   ```

3. Если это не помогло, удалите и создайте базу данных заново:
   ```sql
   DROP DATABASE your_db_name;
   CREATE DATABASE your_db_name WITH OWNER your_db_user;
   GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
   ```

4. Повторите миграции:
   ```bash
   python manage.py migrate
   ```

## Лицензия

Этот проект лицензирован под лицензией MIT.
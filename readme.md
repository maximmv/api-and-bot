Запуск приложения:
docker-compose up --build


Endpoints:

http://localhost/api/v1/rest-auth/registration/
registration

http://localhost/api/v1/rest-auth/login/
login

localhost/api/v1/post/
GET - список постов
POST - создание поста

localhost/api/v1/post/<int:pk>/
GET - чтение поста

localhost/api/v1/authors/
GET - Список авторов

localhost/api/v1/authors/<int:pk>/
GET - Чтение автора

localhost/api/v1/like/
GET - список лайков
POST - создание создание лайка

localhost/api/v1/analytic/?date_from=2020-02-02&date_to=2020-02-15

В деректории с проектом находится скрипт бота ( bot.py ) и файл конфигурации бота 
congig.txt 

Для запуска скрипта нужны requests, Faker

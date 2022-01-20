## Описание проекта
Данное приложение позволяет с помощью API взаимодействовать с базой данных (Сохранять/изменять/получать/удалять данные из БД).
Модель "Персона" включает в себя следующие поля:
- фото
- фамилия
- имя
- отчество
- день рождения
- номер телефона
- статус (не активирован/активирован/удалён)


### Back-End
За основу взят DRF.  
При заходе на сайт, нас встретит The Browsable API - без фронтенда позволяет изучить структуру API и делать запросы.  


#### Примеры запросов:
API доступно по адресу ```/persons/```
#### GET-запросы
- ```/persons/1``` - вернёт пользователя с ID 1. 
- ```/persons/?search=Юрий``` - отдаст результаты поиска по запросу ```Юрий```. 
- ```/persons/?first_name=Юрий&surname=Старовойт``` - отдаст результаты фильтрации по параметрам: ```Имя - Юрий```, ```Фамилия - Старовойт```. 
#### POST-запрос
- ```/persons/``` с корректным телом запроса создаст нового пользователя
#### DELETE-запрос
- ```/persons/1``` - удалит пользователя с ID 1. 


### Front-End
//TODO


### Запуск проекта
Для запуска проекта в "боевом" режиме используйте:  
- ```docker-compose -f docker-compose.prod.yml up -d --build```  
- ```docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput```  
- ```docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear```  

Для запуска проекта в режиме разработчика используйте,
```docker-compose -f docker-compose.yml up -d --build```  



### Используемые библиотеки
 - psycopg2-binary - хендлер для работы с PostgreSQL
 - Django - основной фреймворк
 - djangorestframework - библиотека для создания API и дальнейшей работы с ним 
 - django_filter - фильтрация данных в форме
 - phonenumbers - для хранения и верификации телефонных номеров
 - Pillow - для работы/хранения изображений в Django
 - gunicorn - http-сервер

### Env файлы
- DEBUG=True - Режим отладки (по умолчанию отключен)
- SECRET_KEY=ChangeMe - секретный ключ Django (Обязательна смена перед деплоем)
- DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] - допустимые адреса работы
- SQL_ENGINE=django.db.backends.postgresql - какая база данных используется
- SQL_DATABASE=testcase_db - имя БД
- SQL_USER=testcase_user - пользователь БД
- SQL_PASSWORD=testcase_password - пароль от БД
- SQL_HOST=db - Адрес БД
- SQL_PORT=5432 - порт БД
- DATABASE=postgres - Тип базы данных

##### Данный проект является тестовым заданием

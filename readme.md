### Back-End
За основу взят DRF.  
При заходе на сайт, нас встретит The Browsable API - без фронтенда позволяет изучить структуру API и делать запросы.  


#### Примеры запросов:
API доступно по адресу ```/persons/```
```/persons/1``` - вернёт пользователя с ID 1
```/persons/?search=Юрий``` - отдаст результаты поиска по запросу ```Юрий```
```/persons/?first_name=Юрий&surname=Старовойт``` - отдаст результаты фильтрации по параметрам: ```Имя - Юрий```, ```Фамилия - Старовойт```


### Front-End
//TODO



### Запуск проекта
Для запуска проекта в "боевом" режиме используйте:  
```docker-compose -f docker-compose.prod.yml up -d --build```  
```docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput```  
```docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear```  

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
*КРАЙНЕ НЕ РЕКОМЕНДУЕТСЯ ОСТАВЛЯТЬ .env файлы в репозитории*.  
(В данном случае это сделано для ускорения деплоя и демонстрации для конечного пользователя)
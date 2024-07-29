## Описание проекта.

_**Yellow-watch**_ - сайт на Django 4.2 часового бутика. Основное требование к проекту: иметь некоторое подобие CRM-системы для управления размещёнными заявками и обращениями - реализовано детальной настройкой админ-панели Django. Работа пользователей с товарами на сайте происходит через отправку запроса при нажатии на соответствующую кнопку.

В проекте используется глобальное кеширование через связку `Redis` и библиотеки `django-cachalot`. Так же используется Celery для отправки сообщения на почту пользователя с информацией о созданном заказе.
Обращения из всех форм обрабатываются и отправляются менеджеру telegram-ботом посредством очереди Celery.

В директории проекта находятся два .yml-файла для Docker compose:  
1. `docker-compose.yml` - для локальной сборки без привязки образов к Docker Hub
2. `docker-compose.production.yml` - для сборки на сервере, где установлен и настроен Docker

Код сайт оптимизировался в соответствии с тестированием в `Lighthouse`.

## Используемые технологии.

![Python 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg?style=flat&logo=python&logoColor=white)
![Celery 5.4.0](https://img.shields.io/badge/Celery-5.4.0-brightgreen.svg?style=flat&logo=celery&logoColor=white)
![Redis 5.0.4](https://img.shields.io/badge/Redis-5.0.4-brightgreen.svg?style=flat&logo=redis&logoColor=white)
![Python-telegram-bot 13.7](https://img.shields.io/badge/python--telegram--bot-13.7-brightgreen.svg?style=flat&logo=python&logoColor=white)
![Django 4.2](https://img.shields.io/badge/Django-4.2-brightgreen.svg?style=flat&logo=django&logoColor=white)
![Django-filter 24.2](https://img.shields.io/badge/Django--filter-24.2-brightgreen.svg?style=flat&logo=django&logoColor=white)
![Django-phonenumber-field 8.0.0](https://img.shields.io/badge/Django--phonenumber--field-8.0.0-brightgreen.svg?style=flat&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-brightgreen.svg?style=flat&logo=docker&logoColor=white&color=blue)
![Gunicorn](https://img.shields.io/badge/Gunicorn-brightgreen.svg?style=flat&logo=gunicorn&logoColor=white&color=blue)
![Nginx](https://img.shields.io/badge/Nginx-brightgreen.svg?style=flat&logo=nginx&logoColor=white&color=blue)

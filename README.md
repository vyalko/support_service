# Support_service

## Описание

Микросервисна Django для отправки обращений в саппорт с помощью сервиса django-helpdesk через API. 

## Стек

* Django 5.1.5
* djangorestframework  3.15.2
* Python 3.12.3


## Установка

1. Клонируйте репозиторий на свой компьютер:

```
git clone git@github.com:vyalko/support_service.git
```
```
cd support_service
```

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

## Запуск проекта

1. Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
2. Выполнить миграции:

```
python3 manage.py migrate
```

3. Запустить проект:

```
python3 manage.py runserver
```


Release
0.0.1

Date
January 21, 2025

Saraev Ivan

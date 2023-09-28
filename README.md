# Spend-Revenue statistic

This is a simple API where you can get QuerySets of SpendStatistic and RevenueStatistic models
___
# How to run

To run this project on your machine make the following steps:

* Clone repository to your computer
* Create and activate venv:
```
python -m venv venv
venv\Scripts\activate.bat
```
* Install requirements:
```
pip install -r requirements.txt
```
* Make migrations and apply them:
```
python manage.py makemigrations
python manage.py migrate
```
* Create superuser (optional, but you will need if to create new spends/revenues):
```
python manage.py createsuperuser
```
* Run server:
```
python manage.py runserver
```
___
# Documentation

You can use documentation for this API by this path:
``http://127.0.0.1:8000/api/schema/swagger/``

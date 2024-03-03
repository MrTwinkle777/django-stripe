# Проект DjangoStripe
### Описание
Реализация Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель Item с полями (name, description, price) 
- API с двумя методами:
  - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
  - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Также реализованио:
  - Запуск используя Docker
  - Использование environment variables
  - Просмотр Django Моделей в Django Admin панели
  - Запуск приложения на удаленном сервере, доступном для тестирования (http://alex121221.pythonanywhere.com/item/2)
  - Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте

## Для запуска проекта на локальной машине:
- склонировать репозиторий
- в папке django-stripe задать переменные окружения в файле .env

```bash
SECRET_KEY= Django secret key
DEBUG=True

STRIPE_PUBLISHABLE_KEY='' STRIPE PUBLISHABLE KEY
STRIPE_SECRET_KEY='' STRIPE SECRET KEY
```
Далее:
```bash
docker-compose up --build
```
- Выполняем миграции:
```bash
docker exec django-stripe-web-1 python manage.py makemigrations
docker exec django-stripe-web-1 python manage.py migrate
```
- Создайте суперюзера :
```bash
docker exec -it django-stripe-web-1 python manage.py createsuperuser
```

  

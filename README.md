# DjangoStripePayments
Django and Stripe Payments
Задача

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

```
Реализовано приложение Django 5.0 (Ubuntu 20.04, python 3.10):
  
  - project - каталог djstripe
  
  - application - каталог spays
  
  - db - файл db.sqlite3
  
  - superuser - admin/admin
  
  - зависимости - файл requirements.txt
  
  - settings - djstripe/settings.py
  
  - запуск - python manage.py runserver <host>:<port>
```

·   Django Модель Item с полями (name, description, price)

```
реализовано в spays.models.Item
```

API с двумя методами:

·   GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

```
реализовано в spays.views.CreateSessionView
```

·   GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

```
реализовано в spays.views.ItemView
```

·   Запуск используя Docker

```
реализовано в Dockerfile
```

·   Использование environment variables

```
реализовано в djstripe.settings, 
можно использовать environment variables: 
DJANGO_SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY 
или установить в файле .env
```

·   Просмотр Django Моделей в Django Admin панели

```
реализовано в urls: 
/items, /discounts, /orders, /admin 
(для пользователей - сотрудников)
```

·   Запуск приложения на удаленном сервере, доступном для тестирования

```
реализовано для ansible-playbook: install-remote.yaml 
(необходимо устанавливать поля remote-host, remote-user)
```

·   Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

```
реализовано url: /order, в spays.models.Order, 
в spays.views.OrderView, CreateSessionView
```

·   Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.

```
реализована Discount в spays.models.Discount, 
добавление скидки к заказу доступно для пользователей-сотрудников 
в spays.views.OrderView, CreateSessionView
```

·   Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте

·   Реализовать не Stripe Session, а Stripe Payment Intent.




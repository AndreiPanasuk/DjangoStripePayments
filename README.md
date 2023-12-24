# DjangoStripePayments
Django and Stripe Payments

Задача

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

<div style="color:blue">Реализовано приложение Django (Ubuntu 20.04, python3.10):
  
  - project - каталог djstripe
  
  - application - каталог spays
  
  - db - файл db.sqlite3
  
  - superuser - admin/admin
  
  - зависимости - файл requirements.txt</div>

·   Django Модель Item с полями (name, description, price)

<span style="color:blue">реализовано в spays/models.py (Item)</span>

API с двумя методами:

·   GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

<span style="color:blue">реализовано в spays/views.py (CreateSessionView)</span>

·   GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

<span style="color:blue">реализовано в spays/views.py (ItemView)</span>

·   Запуск используя Docker

<span style="color:blue">реализовано в Dockerfile</span>

·   Использование environment variables

<span style="color:blue">реализовано в djstripe/settings.py, можно использовать environment variables: DJANGO_SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY или установить в файле .env</span>

·   Просмотр Django Моделей в Django Admin панели

<span style="color:blue">реализовано в urls: /items, /discounts, /orders, /admin (для пользователей - сотрудников)</span>

·   Запуск приложения на удаленном сервере, доступном для тестирования

<span style="color:blue">реализовано для ansible-playbook: install-remote.yaml (необходимо устанавливать поля remote-host, remote-user)</span>

·   Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

<span style="color:blue">реализовано url: /order, в spays/models.py (Order), в spays/views.py (OrderView, CreateOrderSessionView)</span>

·   Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.

<span style="color:blue">реализована Discount в spays/models.py (Discount), добавление скидки к заказу доступно для пользователей-сотрудников в spays/views.py (OrderView, CreateOrderSessionView)</span>

·   Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте

·   Реализовать не Stripe Session, а Stripe Payment Intent.




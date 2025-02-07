# Сайт для продажи цветов

Это fullstack e-commerce сайт, построенный на Django для продажи букетов. Он предоставляет функции для управления категориями, добавления товаров в корзину, обработки заказов и онлайн-оплаты через Stripe. Также проект включает асинхронную очередь задач с использованием Celery и RabbitMQ для отправки подтверждающих писем после оформления заказа.

## Особенности

- **Каталог товаров**: Просмотр букетов по категориям.
- **Корзина**: Добавление букетов в корзину, изменение количества и проверка перед оформлением заказа.
- **Обработка заказов**: Создание и управление заказами.
- **Интеграция оплаты**: Безопасная обработка платежей с помощью Stripe.
- **Подтверждение заказа по email**: После оплаты заказа пользователи получают письмо с подтверждением, отправленное с помощью Celery и RabbitMQ.

## Технологический стек

- **Backend**: Django 
- **Frontend**: HTML, CSS, DTL
- **База данных**: SQLite (для локальной разработки)
- **Платежи**: Stripe для онлайн-оплаты
- **Асинхронные задачи**: Celery и RabbitMQ для обработки фоновых задач (отправка email после заказа)

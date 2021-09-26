# help-children-backend


Запуск отдельно приложения в режиме отладки:
`uvicorn app.main:app --reload`

# Основной стек технологий:
* HTML, CSS, JavaScript  - Frontend
* Vue (Nuxt.js) - Frontend
* FastAPI (Python 3) - Backend
* MongoDB - Backend


## Реализованная backend функциональность
1. Расширяемая система хранений данных и аккаунтов;
2. Генерация и создание аккаунтов воспитанников детских домов;
3. Создание достижений из файла и сохранение их в базу;
4. Система авторизации;
5. Простая система чата с комнатами;
6. Качественная расширяемая архитектура проекта в стиле MVC;

## СРЕДА ЗАПУСКА
развертывание backend сервиса производится с помощью docker-compose:
1. https://totaku.ru/ustanovka-docker-i-docker-compose-v-ubuntu-18-04/
2. `docker-compose up -d --build`


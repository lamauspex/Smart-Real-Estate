# Smart Real Estate

> Платформа для управления недвижимостью с ML-прогнозированием цен

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=flat&logo=django)
![DRF](https://img.shields.io/badge/DRF-3.14-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=flat&logo=postgresql)
![ML](https://img.shields.io/badge/ML-ScikitLearn-orange)

## 🟢 Технологический стек

| Компонент | Технология | Назначение |
|-----------|------------|------------|
| Backend | Django 4.2+ | Основной фреймворк |
| API | Django REST Framework | RESTful API |
| База данных | PostgreSQL | Хранение данных |
| Кеширование | Redis | Кеширование и сессии |
| Асинхронные задачи | Celery | Фоновая обработка |
| ML | Scikit-learn | Прогнозирование цен |
| Документация | DRF YASG (Swagger) | Автогенерация API-документации |
| Фильтрация | Django Filters | Фильтрация и поиск |

## 🟢 Ключевые навыки

- **Django** — полноценные веб-приложения
- **Django REST Framework** — REST API
- **PostgreSQL** — работа с реляционной БД
- **Celery + Redis** — асинхронные задачи
- **Машинное обучение** — прогнозирование цен
- **Кеширование** — оптимизация производительности
- **Docker** — готовность к контейнеризации

## 🟢 Возможности

### Управление недвижимостью
- Создание, редактирование, удаление объектов
- Типы объектов (квартира, дом, участок)
- Геолокация (широта/долгота)
- Загрузка изображений
- Статусы объектов (доступно, продано, сдано)

### API
- Полный CRUD для объектов недвижимости
- Пагинация
- Фильтрация по параметрам
- Поиск
- Сортировка
- Токен-аутентификация
- Swagger-документация

### ML-прогнозирование
- Предсказание рыночной цены
- Оценка уверенности модели
- Анализ важности признаков

## 🟢 Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `GET` | `/api/properties/` | Список объектов |
| `POST` | `/api/properties/` | Создание объекта |
| `GET` | `/api/properties/{id}/` | Объект по ID |
| `PUT` | `/api/properties/{id}/` | Обновление объекта |
| `DELETE` | `/api/properties/{id}/` | Удаление объекта |
| `GET` | `/api/ml/predict/{id}/` | Прогноз цены |

## 🟢 Структура проекта

```
Smart-Real-Estate/
├── config/                    # Конфигурация Django
│   ├── settings/              # Настройки (base, dev, prod)
│   ├── celery.py              # Конфигурация Celery
│   ├── urls.py                # Маршруты
│   └── wsgi.py
├── apps/                      # Приложения
│   ├── users/                 # Пользователи
│   ├── properties/            # Недвижимость (CRUD)
│   ├── ml/                    # Машинное обучение
│   └── analytics/             # Аналитика
├── manage.py                  # Управление Django
└── requirements.txt           # Зависимости
```

## 🟢 Быстрый старт


### Клонирование
```bash
git clone https://github.com/lamauspex/Smart-Real-Estate.git
```

### Переход в директорию
```bash
cd Smart-Real-Estate
```

### Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Применение миграций
```bash
python manage.py migrate
```

### Запуск сервера
```bash
python manage.py runserver
```

## 🟢 Настройка переменных окружения

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=smart_real_estate
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
```

## 🟢 Документация API

После запуска доступна по адресу:

```
http://localhost:8000/swagger/
```

## 🟢 Архитектура

```
┌─────────────────────────────────────────────┐
│                 Django                      │
├─────────────────────────────────────────────┤
│  Users  │  Properties  │  ML  │  Analytics  │
├─────────────────────────────────────────────┤
│              Django REST Framework          │
├─────────────────────────────────────────────┤
│     Celery (async tasks)  │  Redis (cache)  │
├─────────────────────────────────────────────┤
│              PostgreSQL                     │
└─────────────────────────────────────────────┘
```

---

**Автор**: Резник Кирилл  
**Email**: lamauspex@yandex.ru  
**Telegram**: @lamauspex  
**GitHub**: https://github.com/lamauspex

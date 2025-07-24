# FastAPI Test Task

## Описание проекта

Это простой REST API, реализованный с помощью FastAPI и Pydantic, для управления сущностями (например, элементами, объектами и т.п.).  
Данные хранятся в оперативной памяти в виде словаря, поэтому все изменения сохраняются только во время работы сервера и теряются при его перезапуске.

### Основной функционал

- Получение списка сущностей с возможностью фильтрации по имени (`GET /entities?name=...`)
- Получение одной сущности по её ID (`GET /entities/{entity_id}`)
- Создание новой сущности (`POST /entities`)
- Обновление существующей сущности (`PUT /entities/{entity_id}`)
- Удаление сущности (`DELETE /entities/{entity_id}`)

### Технологии

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
- ![Pydantic](https://img.shields.io/badge/Pydantic-176C7A?style=for-the-badge&logo=pydantic&logoColor=white)
- ![Uvicorn](https://img.shields.io/badge/Uvicorn-FA704B?style=for-the-badge&logo=uvicorn&logoColor=white)
- ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/s16v6/FastApi.git
cd FastApi
Создайте и активируйте виртуальное окружение:
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
Установите зависимости:
pip install -r requirements.txt
(Если файла requirements.txt нет, установите минимум:)

pip install fastapi uvicorn
Запустите сервер:
uvicorn main:app --reload
Перейдите в браузере по адресу http://127.0.0.1:8000/docs чтобы открыть автоматически сгенерированную документацию Swagger UI.
Структура проекта
FastApi/
├── main.py              # Основной файл с FastAPI приложением и эндпоинтами
├── models.py            # Pydantic модели для сущностей
├── requirements.txt     # Зависимости проекта
├── README.md            # Документация проекта
└── ...
Пример использования API
Получить список сущностей
GET /entities
GET /entities?name=example
Создать новую сущность
POST /entities
Content-Type: application/json

{
  "name": "Example entity",
  "description": "Описание сущности"
}
Обновить сущность
PUT /entities/{entity_id}
Content-Type: application/json

{
  "name": "Новое имя",
  "description": "Новое описание"
}
Удалить сущность
DELETE /entities/{entity_id}
# FastAPI Project



## Описание

Этот проект использует FastAPI для создания простых маршрутов для различных задач, таких как вычисления суммы, числа Фибоначчи и т.д.



## Установка и запуск проекта



### Клонирование репозитория

Клонируйте проект с GitHub:

```bash
git clone https://github.com/smailovdev/api-project.git

```



### Установка виртуального окружения

Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
```



### Установка зависимостей

Установите зависимости проекта с помощью `pip`:

```bash
pip install -r requirements.txt
```



### Запуск проекта

Для запуска FastAPI сервера выполните следующую команду:

```
uvicorn main:app --reload
```

Сервер будет доступен по адресу: `http://127.0.0.1:8000`



### Тестирование API

Для тестирования API используйте `curl` или http://127.0.0.1:8000/docs, где вы найдете автоматически сгенерированную документацию Swagger UI.



### Остановка сервера

Нажмите `Ctrl + C` в терминале, чтобы остановить сервер.
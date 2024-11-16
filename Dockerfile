# Используем базовый образ Python 3.10
FROM python:3.10-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    gcc \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . /app/

# Открываем порт 5005 для доступа к приложению
EXPOSE 8000

# Устанавливаем команду запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

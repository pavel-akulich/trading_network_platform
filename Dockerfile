# Используем официальный образ Python 3.12 в качестве базового
FROM python:3.12

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей в рабочую директорию
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Копируем остальную часть кода приложения в рабочую директорию
COPY . .

# Используйте официальный образ Python
FROM python:3.9

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте requirements.txt в контейнер
COPY requirements.txt .

# Установите зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальные файлы в контейнер
COPY . .

# Укажите порт, который будет использоваться вашим FastAPI-сервисом
EXPOSE 8000

# Укажите команду, которая будет выполняться при запуске контейнера
CMD [ "python", "app.py" ]
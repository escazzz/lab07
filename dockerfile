#задаем базовый образ. Используем образ python
FROM python:3.9.6

#далее импортируем файлы, которые будем запускать
# файл server.py, который в докер-контейнере мы разместим в папке /server/
ADD server.py /server/
RUN pip install requests
#и установим директорию /server в качестве рабочей для контпейнера

WORKDIR /server/

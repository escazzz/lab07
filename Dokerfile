#задаем базовый образ. Используем образ python
FROM python:3.9.6

#далее импортируем файлы, которые будем запускать
# файл client.py, который в докер-контейнере мы разместим в папке /client/
ADD client.py /client/
RUN pip3 install requests
#и установим директорию /server в качестве рабочей для контпейнера

WORKDIR /client/

# test_bewise

Для начала работы сервиса необходимо скопировать файл параметров окружения
```shell script
cp .env.example .env
```

Запустить контейнер
```shell script
docker-compose up  --build -d
```

Применить доступные миграции
```shell script
docker-compose exec web alembic upgrade head
```

После запуска контейнера, можно посмотреть свагер по ссылке: http://127.0.0.1:8000/docs

Завершить работу контейнера
```shell script
docker-compose down
```

***

Пример запроса:

url: http://127.0.0.1:8000

method: post 

body: 
```
{
  "questions_num": 1
}
```

***

# Разработка 

Установка зависимостей для локальной разработки
```shell script
python3 -m pip install --upgrade build
```

Установить модуль в режиме разработки
```shell script
python3 -m pip install --editable .
```

Установить зависимости проекта
```shell script
python3 -m pip install -r requirements.txt
```

Запуск модуля с авто перезапуском
```shell script
python3 -m uvicorn src.__main__:app --reload

```
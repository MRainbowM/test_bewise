# test_bewise

Для запуска сервиса необходимо запустить скрипт start.sh (Для завершения работы контейнера, 
в открывшейся консоли нужно ввести CTRL+C)

После запуска контейнера, можно посмотреть свагер по ссылке: http://127.0.0.1:8000/docs

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
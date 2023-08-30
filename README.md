# О решении

1. Файл db в папку `/db`
2. Файлы csv в папку `/csv`
3. Класс для работы с БД в файле `DB.py`
4. Класс для работы с csv в файле `ErrorProcessing.py`
5. Дата среза устанавливается при использовании метода `get_date_data` класса `ErrorProcessing`
6. В задании не указано, что делать, если в таблицах есть записи, не имеющие пары по error_id. Мной решено было такие записи отсекать, так как в результирующей таблице, как мне показалось, упор именно на ошибки при работе пользователей с сервером.
7. Для замеров по памяти используется `memory-profiler`. При запуске `main.py` результат выводится в консоль.
```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     20.7 MiB     20.7 MiB           1   @profile
     8                                         def main():
     9     20.9 MiB      0.2 MiB           1       task_db = DB('db/cheaters.db')
    10     21.4 MiB      0.5 MiB           1       task_db.create_summary_table()
    11                                         
    12     26.0 MiB      4.6 MiB           1       cheaters = dict(task_db.get_cheaters_rows())
    13                                         
    14     26.0 MiB      0.0 MiB           1       errors_data = ErrorProcessing()
    15                                         
    16     27.9 MiB      1.9 MiB           1       client = errors_data.get_date_data('csv/client.csv', '19.05.2021')
    17     29.4 MiB      1.5 MiB           1       server = errors_data.get_date_data('csv/server.csv', '19.05.2021')
    18                                         
    19     29.5 MiB      0.1 MiB           1       summary_data = errors_data.get_summary_data(client, server)
    20     29.5 MiB      0.0 MiB           1       summary_data = errors_data.remove_cheaters(summary_data, cheaters)
    21                                         
    22     30.6 MiB      1.1 MiB           1       task_db.insert_rows_to_summary(summary_data)
```

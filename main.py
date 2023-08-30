from memory_profiler import profile

from DB import DB
from ErrorProcessing import ErrorProcessing


@profile
def main():
    task_db = DB('db/cheaters.db')
    task_db.create_summary_table()

    cheaters = dict(task_db.get_cheaters_rows())

    errors_data = ErrorProcessing()

    client = errors_data.get_date_data('csv/client.csv', '19.05.2021')
    server = errors_data.get_date_data('csv/server.csv', '19.05.2021')

    summary_data = errors_data.get_summary_data(client, server)
    summary_data = errors_data.remove_cheaters(summary_data, cheaters)

    task_db.insert_rows_to_summary(summary_data)


if __name__ == "__main__":
    main()

from datetime import datetime as dt, timedelta
import csv


class ErrorProcessing:

    @classmethod
    def get_date_data(cls, data_file, date):
        date = dt.strptime(date, '%d.%m.%Y').date()
        with open(data_file, encoding='utf-8') as client_file:

            return [row for row in csv.DictReader(client_file) if
                    date == dt.fromtimestamp(int(row['timestamp'])).date()]

    @classmethod
    def get_summary_data(cls, client_data, server_data):
        res_dict = {row['error_id']: [row] for row in client_data}
        for row in server_data:
            if res_dict.get(row['error_id']):
                res_dict.get(row['error_id']).append(row)

        return {k: v for k, v in res_dict.items() if len(v) > 1}

    @classmethod
    def remove_cheaters(cls, summary_data, cheaters_data):
        res_dict = {}
        for k, v in summary_data.items():
            if cheaters_data.get(int(v[0]['player_id'])):
                ban_dt = dt.strptime(cheaters_data.get(int(v[0]['player_id'])), '%Y-%m-%d %H:%M:%S')
                server_dt = dt.fromtimestamp(int(v[1]['timestamp']))
                if server_dt - timedelta(days=1) >= ban_dt:
                    continue
            res_dict[k] = v

        return [(v[1]['timestamp'], v[0]['player_id'], v[1]['event_id'], v[0]['error_id'],
                 v[1]['description'], v[0]['description']) for v in res_dict.values()]

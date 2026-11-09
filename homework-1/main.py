import psycopg2
import csv


def fill_table_from_csv(table_name: str, file_name: str) -> None:
    """ Принимает имя таблицы и имя файла, заполняет таблицу в базе данных. """
    conn = psycopg2.connect(
        dbname = 'north',
        user = 'postgres',
        password = '12345',
        port = '5432',
        host = 'localhost'
    )
    cursor = conn.cursor()

    with open(file_name, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            query = f"INSERT INTO {table_name} ({','.join(header)})  VALUES ({','.join(['%s'] * len(row))})"
            cursor.execute(query, row)

    conn.commit()
    cursor.close()
    conn.close()


def main() -> None:
    """ Скрипт для заполнения данными таблиц в БД Postgres."""
    fill_table_from_csv('employees', 'north_data/employees_data.csv')
    fill_table_from_csv('customers', 'north_data/customers_data.csv')
    fill_table_from_csv('orders', 'north_data/orders_data.csv')


if __name__ == '__main__':
    main()

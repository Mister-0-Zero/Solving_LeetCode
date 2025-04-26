import pandas as pd
import sqlite3


def process(customers, transactions):
    transactions = transactions[
        (transactions['success_flg'] == 1) &
        (transactions['amount_rur'] <= 1_000_000)
        ]

    transactions = transactions.sort_values(['customer_id', 'transaction_dttm'])

    transactions['prev_amount'] = transactions.groupby('customer_id')['amount_rur'].shift(1)
    transactions['next_amount'] = transactions.groupby('customer_id')['amount_rur'].shift(-1)

    mask = (
            (transactions['amount_rur'] > transactions['prev_amount']) &
            (transactions['amount_rur'] > transactions['next_amount']) &
            (transactions['next_amount'].notnull())
    )
    res = transactions[mask]

    res = res.merge(customers[['id', 'name']], left_on='customer_id', right_on='id', how='left')

    return res[['name', 'id_x']].rename(columns={'name': 'customer_name', 'id_x': 'transaction_id'})

conn = sqlite3.connect(r'data\data.db')  # путь к твоему файлу .db

# Загружаем таблицу transactions
transactions = pd.read_sql_query("SELECT * FROM transactions", conn)

# Загружаем таблицу customer
customers = pd.read_sql_query("SELECT * FROM customer", conn)

res = process(customers, transactions)
print(res)

# Закрываем соединение (лучше всегда закрывать после работы)
conn.close()
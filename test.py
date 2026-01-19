# import mysql.connector
#
# DB_CONFIG = {
#     'host':'localhost',
#     'port': 3306,
#     'user':'root',
#     'password':'root',
#     'database':'sakila'
# }
# # headers = ['id', 'name', 'species','birth_year']
# def get_conn():
#     return mysql.connector.connect(**DB_CONFIG)
#
# def load_actors():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute('select * from actor')
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     print(rows)
# load_actors()

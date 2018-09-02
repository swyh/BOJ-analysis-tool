import sqlite3 as lite

def connect(file_name, load_table_name = ""):
    global conn
    global cs
    global table_name

    if load_table_name != "":
        table_name = load_table_name

    conn = lite.connect(file_name)
    cs = conn.cursor()


def create_table(create_table_name):

    table_name = create_table_name

    query = "DROP TABLE IF EXISTS {0}".format(create_table_name)
    cs.execute(query)

    query = "CREATE TABLE IF NOT EXISTS {0} (id INTEGER PRIMARY_KEY NOT_NULL, name VARCHAR(255), percent INTEGER)".format(table_name)
    cs.execute(query)


def insert(list):
    for i in range(len(list)):
        query = "INSERT into {0} values (?, ?, ?)".format(table_name)
        cs.execute(query, (list[i][0], list[i][1], list[i][2]))
    conn.commit()


def select_all():
    query = "SELECT * FROM {0}".format(table_name)
    cs.execute(query)
    all_rows = cs.fetchall()

    list = []
    for i in all_rows:
        #print(i)
        list.append(i)

    return list

def select(number):
    query = "SELECT percent FROM {0} WHERE id = {1}".format(table_name, number)
    cs.execute(query)
    percent = cs.fetchall()

    return percent[0][0]
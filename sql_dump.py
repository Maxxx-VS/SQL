import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    with open("sql_damp.sql", "w") as f: # создать дамп БД
        for sql in con.iterdump():
            f.write(sql)

    with open("sql_damp.sql", "r") as f: # восстановить потрянную БД
        sql = f.read()
        cur.executescript(sql)
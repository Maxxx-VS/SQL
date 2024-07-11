import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS users")

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER)
    """)

    cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57246)")
    cur.execute("INSERT INTO cars VALUES(3, 'Skoda', 9000)")
    cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
    cur.execute("INSERT INTO cars VALUES(5, 'Bentlt', 350000)")


    # for result in cur:
    #     print(result)

    # result_1 = cur.fetchone()
    # print(result_1)
    #
    # result_2 = cur.fetchmany(2)
    # print(result_2)
import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Mercedes', 57246),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentlt', 350000)
]

con = None
try:
    con = sq.connect("cars.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER)
    """)

    cur.executescript("""
        DELETE FROM cars WHERE model LIKE 'A%';
        UPDATE cars SET price = price+1000
    """)

    con.commit() # сохраняет в БД все изменения

except sq.Error as e:
    if con: con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con: con.close()

    # with sq.connect("cars.db") as con:
    #     cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS users")





    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})

    # ДОБАВЛЕНИЕ В БД executemany
    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)


    # ДОБАВЛЕНИЕ В БД ЦИКЛОМ
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)



    # ПРОСТОЕ ДОБАВЛЕНИЕ В БД ПОСТРОЧНО
    # cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57246)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Skoda', 9000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Bentlt', 350000)")





    # for result in cur:
    #     print(result)

    # result_1 = cur.fetchone()
    # print(result_1)
    #
    # result_2 = cur.fetchmany(2)
    # print(result_2)
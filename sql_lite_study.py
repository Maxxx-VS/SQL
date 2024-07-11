import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS users")

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")


    # for result in cur:
    #     print(result)

    result_1 = cur.fetchone()
    print(result_1)

    result_2 = cur.fetchmany(2)
    print(result_2)
import sqlphile as sp 

with sp.sqlite3(r'database.db') as db:
    q = (db.insert("users")
        .data(_id=1, username="John", email= "johndoe@gmail.com")
        .execute())

    q = (db.select("users")
        .get("id", "name", "email")
        .filter())

for row in q.fetchall():
    print(row)


####### ---OR--- #######

with sp.sqlite3("database.db3", dir="./sqlmap") as db:
    rows = (db.file.get_stat.filter(id = 1, name__startswith = "J")
            .execute()
            .fetchall())

## Introduction

Sqlphile is a SQL template engine and python style SQL generator. It looks like ORM (Object Relational Mapper) but it has no relationship with ORM. 

Many SQL Template Engines lets us to query the database in our own scripts but the query should be written in SQL. 

It is inspired mainly by <b>Django ORM</b> and <b>iBATIS SQL Maps</b>.

<b>iBATIS</b> is a persistence framework which automates the mapping between SQL database objects (e.g. tables) and objects in Java (e.g. user defined class or collection object). This mapping is created and maintained using xml configuration files. These configuration files contain various SQL statements and other framework related options. 

The <b>Django</b> web framework includes a default object-relational mapping layer (ORM) that can be used to interact with application data from various relational databases such as SQLite, PostgreSQL and MySQL.

SQLPhile also does the same thing but it writes the queries into different template SQL files.

Here's an basic example to use SQLPhile, 
 
~~~~
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
~~~~

This makes the script so confusing if we have many bigger query statements. <b>SQLPhile</b> is useful for keeping clean look the scripts there by hiding SQL statements making it the pythonic way by using python functions.  

The above code can be written with SQLPhile:
~~~~
import sqlphile as sp

with sp.mysql("dbname", "user", "password", "server") as db:
    rows = (db.select("customers")
           .data(name = "John", address="Highway 21")
           .excecute())
~~~~

Or we can use SQL Template files in the way the iBATIS does .

sqlmaps/file.sql

~~~~
<sql name="get_stat">
    SELECT name FROM customers 
    WHERE {this.filters}
</sql>
~~~~

This can be accessed by the name property in our script 

~~~~
with sp.mysql("mydatabase.db", dir="./sqlmap) as db:
    rows = (db.file.get_stat.filter(name__startswith="J")
           .excecute()
           .fetchall())
~~~~




## Introduction

<b>PugSQL</b> is a simple Python interface for organizing and using parameterized, handwritten SQL. It is an <b>anti-ORM</b> that is philosophically lo-fi, but it still presents a clean interface in Python.

It is inspired by <b>HugSQL</b> library which uses simple conventions in your SQL files to define database functions, thereby creating a clean seperation of Clojure Code and SQL code.

It is a replacement of ORM in Python which supports the db's supported by SQLAlchemy, by seperating the SQL Code and Python Script. 
 
<ol>
    <li> Firstly in a PugSQL project the sql files are stored in a directory. <b>(.sql files) </b>
    </li>
    <br>
    <li> The .sql files contain special leading comments to specify the names of the queries. 
    </li>
    <br>
    <li> These files will contain the <b>sql queries</b>, these contain queries and desired return types. These queries can return a single row or many rows. 
    </li>
    <br>
    <li> These queries can be imported as modules and can be used in a pythonic way.
    </li>
    <br>
</ol>

.sql file sample

~~~~
-- :name user_for_id :one
select * from users where user_id = :user_id
~~~~

The python code can be given as,

~~~~
import pugsql

queries  = pugsql.module('queries/')

queries.connect('sqlite:///path-to-db/dbname')
queries.update_user_name(user_id=42, username='John Doe')

~~~~

The return values are returned as Dictionaries and the return types of the values depend on the desired return types used in the .sql files. 
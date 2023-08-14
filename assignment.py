#Ans-1 A database is an organized collection of structured information, or data, typically stored electronically in a 
# computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the 
# applications that are associated with them, are referred to as a database system, often shortened to just database.
# DIFFERENCES BETWEEN SQL AND NOSQL:-
#  SQL databases are relational, and NoSQL databases are non-relational.
#SQL databases use structured query language (SQL) and have a predefined schema. NoSQL databases have dynamic schemas for unstructured data.
#SQL databases are vertically scalable, while NoSQL databases are horizontally scalable.
#SQL databases are table-based, while NoSQL databases are document, key-value, graph, or wide-column stores.
#SQL databases are better for multi-row transactions, while NoSQL is better for unstructured data like documents or JSON.

#Ans-2 A data definition language (DDL) is a computer language used to create and modify the structure of database objects in a database. 
# These database objects include views, schemas, tables, indexes, etc.
#The CREATE TABLE command creates a new table in the database.

#The following SQL creates a table called "Persons" that contains five columns: PersonID, LastName, FirstName, Address, and City:

#Example
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
"CREATE TABLE Persons (PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar(255), City varchar(255))"
mydb.close()

#ALTER TABLE
# ALTER TABLE command adds, deletes, or modifies columns in a table.
#The ALTER TABLE command also adds and deletes various constraints in a table.

"ALTER TABLE Customers(ADD EMAIL VARCHAR(255)"

#The DROP TABLE command deletes a table in the database.
"DROP TABLE Shippers"

#The TRUNCATE TABLE command deletes the data inside a table, but not the table itself.
"TRUNCATE TABLE Categories"

#Ans-3 A data manipulation language (DML) is a family of 
# computer languages including commands permitting users to
#  manipulate data in a database. This manipulation involves 
# inserting data into database tables, retrieving existing data,
#  deleting data from existing tables and  modifying existing data.
#  DML is mostly incorporated in SQL databases.

#he SQL INSERT, UPDATE, and DELETE commands enable SQL users to 
# manipulate and modify data:
#The INSERT statement introduces new rows into an existing table.
#The DELETE statement removes a row or combination of rows from a table.
#The UPDATE statement enables users to update a row or group of rows in a table.

#Ans-4 DQL is a portion of a SQL statement that allows you
#  to get and organise data from a database. You can use the SELECT 
# command to extract data from a database in order to perform actions on it. It is the same
#  as the projection operation in relational algebra. The result of a SELECT statement on a 
# table or collection  of tables is compiled into a new temporary table, which is subsequently
#  displayed or received by a program, i.e. a front-end.

#Example
#SELECT Stu_Name FROM Student WHERE Phone = 9039462908;

#Ans-5 A primary key is used to ensure data in the specific column is unique. 
# A foreign key is a column or group of columns in a relational 
# database table that provides a link between data in two tables.

#Ans-6
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

#A cursor is an object which helps to execute the query and fetch the 
# records from the database. The cursor plays a very important role in executing the query. 

#ANS-7  The order is:
#1 FROM 
#2 HERE
#3 GROUP BY
#4 HAVING
#5 SELECT
#6 ORDER BY
#7 LIMIT
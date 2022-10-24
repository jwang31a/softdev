# How to SQLite by Team Spooky :: Jun Hong Wang, James Yu, Thomas Zhang

## The Basics
* First, open SQLite in the terminal by typing `sqlite3`, which opens the SQLite shell. From here, we can work on tables through commands. 
* You can type `.help` to get a detailed list of commands. 
* To make a new table, type `CREATE TABLE <name> (<column name> <data type>, ...);`
* To see all the tables you've made, type `.tables`. 
* To insert a new item into the table, use `INSERT INTO <table_name> VALUES (<field 1>,<field 2>, ...);`
* To remove from a table, use `DELETE FROM <table_name> WHERE <condition>;`
* To see what has been added to the table, use `SELECT * FROM <table_name>;`. The * represents the wildcard operator, which means everything in this file in this case. 
* By default, SQLite shows the contents of a table by separating the fields of each entry with a `|`. To change this, use `.mode <mode_name>`. Each mode displays the content a little differently. Below are examples of different modes. 
	* Column:<br>name   number<br>-----  ------<br>name1  1<br>name2  2<br>name3  3
	* CSV:<br>name,number<br>name1,1<br>name2,2<br>name3,3
	* INSERT: <br>INSERT INTO "table"(name,number) VALUES('name1',1);<br>INSERT INTO "table"(name,number) VALUES('name2',2);<br>INSERT INTO "table"(name,number) VALUES('name3',3);
* To select a whole column, use `SELECT <column_name> FROM <table_name>;`
* To select an entry that satisfies certain requirements, use the WHERE keyword to filter results by using `SELECT * FROM <table_name> WHERE <field_name> = <value>;`
* To quit the shell, type `.quit`.
* The tables you name in the shell don't save, unless you do `.once FileName.sql`, which directs the output of the next command into the file. Then, you can do `.dump`, which puts all the commands needed to reconstruct the table into that file. 
 
## Interesting Observations
* **Make sure you have semicolons at the end of each line of SQL.** This is very important, and making sure you put semicolons will save you a lot of time.
* For commands starting with `.`, don't put a semicolon after. 
* None of the commands actually have to be capitalized, so as long as the right word is entered, it seems like it will work. (however, it seems that capitalization is standard for maximum readability)
* .header toggles the column name

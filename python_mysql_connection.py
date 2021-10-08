import mysql.connector

username = input("enter username: ")               #enter username of your mysql db
databasename = input("enter database name: ")      #enter database which you want to work with
password = input("enter password: ")               #enter password of your mysql db
hostname = input("enter hostname: ")		   #enter host name 


try:
    conn = mysql.connector.connect(user = username, database=databasename, password = password, host= hostname, port= 3306)
    cursor = conn.cursor()

    #creating a table in the mentioned data base
    mySql_Create_Table_Query = """CREATE TABLE emp ( 
                                 e_no int NOT NULL PRIMARY KEY ,
                                 ename varchar(250) NOT NULL,
                                 designation varchar(250) NOT NULL,
                                 sal int,
                                 mgr int,
                                 deptno int,
                                 FOREIGN KEY (deptno) REFERENCES dept(deptno)) """

    cursor = conn.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
except mysql.connector.ProgrammingError:
    print("Table Name is already exist in the mentioned data base..!")
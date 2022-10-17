import mysql.connector



## Intiate Connection with MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

mycursor = mydb.cursor(buffered=True)


mycursor.execute("Create database IF NOT EXISTS task1")  #Create the database if it doesnt exist

mycursor.execute("use task1")  #Use the current database

## Create "student" Table
mycursor.execute('''Create table IF NOT EXISTS student (
                        ID int AUTO_INCREMENT,
                        firstName varchar(50),
                        lastName varchar(50),
                        age int,
                        primary key (ID),
                        constraint ageCheck check (age >= 16),
                        constraint UC_name unique (firstName, lastName)
                        )
                ''')


sql = "INSERT INTO student(ID, firstName, lastName, age) VALUES (%s,%s,%s,%s)"
data = [
    (1, "Ahmad", "Tamer", 21),
    (2, "Ahmad", "Ali", 24),
    (3, "Osama", "Elzero", 28),
    (4, "Mohammed", "Tamer", 21),
    # (5, "Ahmad","Tamer",100),              # Violates UC_name constraint
    # (4, "aaa", "a",50),                    # Duplicate Primary key
    # (10, "aaa", "aaaaa", 10)               # Violates ageCheck Constraint

]

try:
    mycursor.executemany(sql, data)
except Exception as e:
    Error = str(e).split(": ",1)[1];
    print(Error)
else:
    print("Success,", mycursor.rowcount, "records were" if (mycursor.rowcount > 1) else "record was" , "inserted.")


## Commit Changes
mydb.commit()


mycursor.execute("DROP database task1")
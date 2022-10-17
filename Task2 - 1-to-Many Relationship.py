import mysql.connector



## Intiate Connection with MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

mycursor = mydb.cursor(buffered=True)


mycursor.execute("Create database IF NOT EXISTS task2")  #Create the database if it doesnt exist
mycursor.execute("use task2")  #Use the current database

## Create "persons" Table
mycursor.execute('''Create table IF NOT EXISTS persons (
                        PersonID int not null AUTO_INCREMENT,
                        firstName varchar(50),
                        lastName varchar(50),
                        age int,
                        primary key (PersonID)
                        )
                ''')

## Create "orders" Table
mycursor.execute('''Create table IF NOT EXISTS orders (
                        OrderID int PRIMARY KEY AUTO_INCREMENT,
                        OrderNumber int not null UNIQUE,
                        PersonID int,
                        FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
                        )
                ''')


# 1-to-Many:
#     Each order has only 1 person
#     but Each person can have Many orders.
#

################### Populating Persons Table
PersonsSQL = "INSERT INTO persons(PersonID, firstName, lastName, age) VALUES (%s,%s,%s,%s)"
PersonsData = [
    (1, "Ahmad", "Tamer", 21),
    (2, "Ahmad", "Ali", 24),
    (3, "Osama", "Elzero", 28),
    (4, "Mohammed", "Tamer", 21),
]

try:
    mycursor.executemany(PersonsSQL, PersonsData)
except Exception as e:
    Error = str(e).split(": ",1)[1];
    print(Error)
else:
    print("Insertion Success in Persons Table,", mycursor.rowcount, "records were" if (mycursor.rowcount > 1) else "record was" , "inserted.")


################### Populating Orders Table
OrdersSQL = "INSERT INTO orders(OrderNumber, PersonID) VALUES (%s,%s)"
OrdersData = [
    (53282, 2),
    (74982, 3),
    (27982, 4),
    (64282, 4),
    (97982, 4),
    (2431182, 1),
    (1123412, 1),
   ## (53282, 2), ## Error, Duplicate entry for the OrderNumber... Violates the 1-to-Many relationship

]

try:
    mycursor.executemany(OrdersSQL, OrdersData)
except Exception as e:
    Error = str(e).split(": ",1)[1];
    print(Error)
else:
    print("Insertion Success in Orders Table,", mycursor.rowcount, "records were" if (mycursor.rowcount > 1) else "record was" , "inserted.")



## Commit Changes
mydb.commit()

# mycursor.execute("DROP database task2")



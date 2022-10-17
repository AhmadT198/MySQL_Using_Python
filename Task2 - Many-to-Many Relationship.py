import mysql.connector

## Intiate Connection with MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("Create database IF NOT EXISTS task2")  # Create the database if it doesnt exist
mycursor.execute("use task2")  # Use the current database

## Create "students" Table
mycursor.execute('''Create table IF NOT EXISTS students (
                        studentID int not null,
                        firstName varchar(50),
                        lastName varchar(50),
                        age int,
                        primary key (studentID)
                        )
                ''')

## Create "courses" Table
mycursor.execute('''Create table IF NOT EXISTS courses (
                        courseID varchar(20) not null,
                        courseName varchar(50) not null,
                        PRIMARY KEY (courseID)
                        )
                ''')

## Create "pivot" Table
mycursor.execute('''Create table IF NOT EXISTS pivot (
                        courseID varchar(20) not null,
                        studentID int not null,
                        foreign key (courseID) references courses(courseID),
                        foreign key (studentID) references students(studentID)
                        )
                ''')




# Many-to-Many:
#     Each Student can have many courses
#     and Each course can have Many enrolled students.
#




############################################################################# Populating Students Table
studentsSQL = "INSERT INTO students(studentID, firstName, lastName, age) VALUES (%s,%s,%s,%s)"
studentsData = [
    (1, "Ahmad", "Tamer", 21),
    (2, "Ahmad", "Ali", 24),
    (3, "Osama", "Elzero", 28),
    (4, "Mohammed", "Tamer", 21),
]

try:
    mycursor.executemany(studentsSQL, studentsData)
except Exception as e:
    Error = str(e).split(": ", 1)[1];
    print("Error while inserting in students Table : ", Error)
else:
    print("Insertion Success in Students Table,", mycursor.rowcount,
          "records were" if (mycursor.rowcount > 1) else "record was", "inserted.")






############################################################################## Populating Courses Table
coursesSQL = "INSERT INTO courses(courseID, courseName) VALUES (%s,%s)"
coursesData = [
    ("CCE213", "Maths"),
    ("PSE223", "Physics"),
    ("CS50", "Maths"),
    ("CES2311", "Maths"),
]

try:
    mycursor.executemany(coursesSQL, coursesData)
except Exception as e:
    Error = str(e).split(": ", 1)[1];
    print("Error while inserting in courses Table : ",Error)
else:
    print("Insertion Success in Courses Table,", mycursor.rowcount,
          "records were" if (mycursor.rowcount > 1) else "record was", "inserted.")





################################################################ Populating Pivot Table and creating Relations
pivotSQL = "INSERT INTO pivot(courseID,studentID) VALUES (%s,%s)"
pivotData = [
    ("CCE213", 1),
    ("PSE223", 1),
    ("CS50", 1),
    ("CES2311", 1),

    ("CCE213", 2),
    ("PSE223", 2),
    ("CS50", 2),
    
    ("CCE213", 3),
    ("PSE223", 3),
    ("CES2311", 3),

]

try:
    mycursor.executemany(pivotSQL, pivotData)
except Exception as e:
    Error = str(e).split(": ", 1)[1];
    print("Error while inserting in the pivot Table : ",Error)
else:
    print("Insertion Success in Pivot Table,", mycursor.rowcount,
          "records were" if (mycursor.rowcount > 1) else "record was", "inserted.")



## Commit Changes
mydb.commit()

mycursor.execute("DROP database task2")

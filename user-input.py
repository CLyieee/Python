import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student"
)
    
mycursor = db.cursor()

def insert():
    full_name = input("Enter your full name: ")
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")

    sql = "INSERT INTO student (full_name, gender, age) VALUES (%s, %s, %s)"
    val = (full_name, gender, age)
    mycursor.execute(sql, val)

    db.commit()

    print("Data has been added")

def update():
    column = input("Enter the column you want to update: ")
    full_name = input("Enter the full name of the person: ")
    new = input("Enter the new value: ")

    sql = f"UPDATE student SET {column} = %s WHERE {column} AND full_name = %s"
    val = (new, full_name)

    mycursor.execute(sql, val)
    db.commit()

def display():
    mycursor.execute("SELECT * FROM student")

    result = mycursor.fetchall()

    for x in result:
        print(x)


def delete():
    column = input("Enter what you want type to remove: ")
    remove = input("Enter value you want to remove: ")

    sql = f"DELETE FROM student WHERE {column} = %s"
    val = (remove,)

    mycursor.execute(sql, val)
    db.commit()

print("Welcome to your Database")

while True:
    print("\nMenu:")
    print("1. Add new Student")
    print("2. Update Student")
    print("3. Display Student")
    print("4. Remove Student")
    print("0. Exit")

    ans = input("Enter choice (0 to exit): ")

    if ans == '1':
        insert()
    elif ans == '2':
        update()
    elif ans == '3':
        display()
    elif ans == '4':
        delete()
    elif ans == '0':
        print("Exiting the program.")
        break
    else:
        print("Wrong Input")

# Close the cursor and connection when done
mycursor.close()
db.close()
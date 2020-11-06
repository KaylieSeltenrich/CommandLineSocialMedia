import dbcreds
import mariadb
import viewallexploits

conn = None
cursor = None

try:

    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
    cursor = conn.cursor()
    alias = input("Please type your alias: ")
    password = input("Please type your password: ")
    cursor.execute("SELECT * FROM hackers WHERE alias=? AND password=?", [alias,password,])
    cursor.fetchall()
    if(cursor.rowcount == 1):
        print("User Login Successful!")
        print("Select an Option:\n 1. Create an exploit\n 2. See all of your exploits\n 3. See all other aliases exploits\n 4. Exit the application")
        user_choice = input("Enter your Option: ")
        if user_choice == "1":
           
        elif user_choice == "2":
           
        elif user_choice == "3":
            viewallexploits.ViewAllExploits()

        elif user_choice == "4":
            
        else: 
            print("Please try again, invalid input!")
    else: 
        print("Try again!")


except mariadb.ProgrammingError:
    print("Programming Error!")

except mariadb.OperationalError:
    print("There seems to be something wrong with the connection.")


finally:
    if(cursor != None):
        cursor.close()
    if(conn != None):
        conn.rollback()
        conn.close()
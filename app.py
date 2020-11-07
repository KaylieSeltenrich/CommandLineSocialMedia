import dbcreds
import mariadb
import functions

conn = None
cursor = None

try:

    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
    cursor = conn.cursor()
    alias = input("Please type your alias: ")
    password = input("Please type your password: ")
    cursor.execute("SELECT * FROM hackers WHERE alias=? AND password=?", [alias,password,])
    user = cursor.fetchone()
    if user:
        print("User Login Successful!\n --------------------------")
    while True:
        print("Select an Option:\n 1. Create an exploit\n 2. See all of your exploits\n 3. See all other aliases exploits\n 4. Exit the application \n --------------------------")
        user_choice = input("Enter your Option: ")
       
        if user_choice == "1":
            functions.CreateExploit(user)
        
        elif user_choice == "2":
            functions.ViewYourExploits(user)
        
        elif user_choice == "3":
            functions.ViewOthersExploits(user)
            
        elif user_choice == "4":
            print("--------------------------\n Good-Bye!")
            break
             
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
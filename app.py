import dbcreds
import mariadb
import functions

conn = None
cursor = None

try:
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
    cursor = conn.cursor()
    print("Welcome to Hackers Social Media. Select an Option:\n 1.Login \n 2.Signup")
    user_welcomechoice = input("\nEnter your Option:")
    if user_welcomechoice == "1":
        alias = input("Please type your alias: ")
        password = input("Please type your password: ")
        cursor.execute("SELECT * FROM hackers WHERE alias=? AND password=?", [alias,password,])
        user = cursor.fetchone()
    elif user_welcomechoice == "2":
        functions.CreateNewUser()
        user = None
    else: 
        print("Error! Please Try Again.")

    if user != None:
        if password == user[2]:
            print("User Login Successful!\n --------------------------")
            while True:
                print("\nSelect an Option:\n 1. Create an exploit\n 2. See all of your exploits\n 3. See all other aliases exploits\n 4. Exit the application \n --------------------------")
                user_choice = input("\nEnter your Option: ")
       
                if user_choice == "1":
                    functions.CreateExploit(user)
        
                elif user_choice == "2":
                    functions.ViewYourExploits(user)
        
                elif user_choice == "3":
                    functions.ViewOthersExploits(user)
            
                elif user_choice == "4":
                    print("--------------------------\nGood-Bye!")
                    break
             
                else: 
                    print("Please try again, invalid input!")
    else: 
        print("--------------------------\nTry again! Invalid user or password.")


except mariadb.ProgrammingError:
    print("Programming Error!")

except mariadb.OperationalError:
    print("There seems to be something wrong with the connection.")

except mariadb.IntegrityError:
    print("That would have damaged the database!")

except mariadb.InternalError:
    print("Internal error of database!")


finally:
    if(cursor != None):
        cursor.close()
    if(conn != None):
        conn.rollback()
        conn.close()
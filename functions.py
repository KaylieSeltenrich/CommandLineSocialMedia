import dbcreds
import mariadb

def CreateExploit(user):
    try:
        content = input("Write your exploit: ")
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO exploits (content, user_id) VALUES(?, ?)", [content, user[0],])
        conn.commit()
        print("--------------------------\n Exploit added succesfully! \n--------------------------" )
        cursor.close()
        conn.close()
    
    except mariadb.ProgrammingError:
        print("Programming Error!")

    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
     
    except mariadb.IntegrityError:
        print("That would have damaged the database!")

    except mariadb.InternalError:
        print("Internal error of database!")



def ViewYourExploits(user,alias):
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits WHERE user_id = ?", [user[0],])
        posts = cursor.fetchall()
        for post in posts:
            print("\ncontent: " + str((post[1])))

    except mariadb.ProgrammingError:
        print("Programming Error!")

    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
    
    except mariadb.IntegrityError:
        print("That would have damaged the database!")

    except mariadb.InternalError:
        print("Internal error of database!")



def ViewOthersExploits(user):
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT hackers.alias, hackers.id, exploits.content FROM exploits INNER JOIN hackers ON exploits.user_id = hackers.id WHERE exploits.user_id != ?", [user[0],])
        posts = cursor.fetchall()
        for post in posts:
            print("\nalias: " + str((post[0])))
            print("\ncontent: " + str((post[2])))

    except mariadb.ProgrammingError:
        print("Programming Error!")

    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
        
    except mariadb.IntegrityError:
        print("That would have damaged the database!")

    except mariadb.InternalError:
        print("Internal error of database!")


def CreateNewUser():

    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
    cursor = conn.cursor()
    alias = input("Please type your alias: ")
    password = input("Please type your password: ")
    if(len(password) < 6):
        print("Password too short!")
    else:
        cursor.execute("INSERT INTO hackers(alias,password) VALUES (?,?)", [alias, password])
        conn.commit()
        if(cursor.rowcount == 1):
            print("User created!")
        else:
            print("Error: User not created.")


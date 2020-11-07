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

    except:
        print("An unanticipated error has occured.")

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

    except:
        print("An unanticipated error has occured.")

def ViewOthersExploits(user):
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits WHERE user_id != ?", [user[0],])
        posts = cursor.fetchall()
        for post in posts:
            print("\nalias: " + alias[2])
            print("\ncontent: " + str((post[1])))

    except mariadb.ProgrammingError:
        print("Programming Error!")

    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
        
    except mariadb.IntegrityError:
        print("That would have damaged the database!")

    except mariadb.InternalError:
        print("Internal error of database!")

    except:
        print("An unanticipated error has occured.")
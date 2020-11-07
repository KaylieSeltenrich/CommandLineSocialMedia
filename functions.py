import dbcreds
import mariadb

def CreateExploit(user):
    content = input("Write your exploit: ")
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO exploits (content, user_id) VALUES(?, ?)", [content, user[0],])
    conn.commit()
    print("Exploit added succesfully!")
    cursor.close()
    conn.close()

def ViewYourExploits(user):
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exploits WHERE user_id = ?", [user[0],])
    posts = cursor.fetchall()
    for post in posts:
        print("exploits id: " + str((post[0])))
        print("content: " + str((post[1])))

def ViewOthersExploits(user):
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exploits WHERE user_id != ?", [user[0],])
    posts = cursor.fetchall()
    for post in posts:
        print("exploits id: " + str((post[0])))
        print("content: " + str((post[1])))
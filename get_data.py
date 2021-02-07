import mysql.connector as co

def get_match():
    match_list = []
    try:
        conn = co.connect(user="admin",
                          password="2AMhpdFJ8WbMOgDWoE2z",
                          host="plfranc.ctjpvwq07ek9.us-east-2.rds.amazonaws.com",
                          port="3306",
                          database="Tennis"
                          )
        print (conn)
        cur = conn.cursor()
        # execute the INSERT statement
        sql_statement = "SELECT * FROM Matchs"
        cur.execute(sql_statement)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            match_list.append(row)
            print(type(row))
        cur.close()
    except co.Error as error:
        print("Failed to insert record into match table {}".format(error))

    finally:
        if (conn.is_connected()):
            conn.close()
            print("MySQL connection is closed")

            return match_list
import mysql.connector as co


def get_match():
    match_list = []
    try:

        conn = co.connect(user="admin",
                          password="2AMhpdFJ8WbMOgDWoE2z",
                          host="aaoi655qep0ekl.ctjpvwq07ek9.us-east-2.rds.amazonaws.com",
                          port="3306",
                          database="ebdb"
                          )

        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql_statement = "SELECT * FROM Matchs"
            cur.execute(sql_statement)
            while True:
                row = cur.fetchone()
                if row == None:
                    break
                match_list.append(row)

            cur.close()
            if (conn.is_connected()):
                conn.close()

                return match_list
        except co.Error as error:
            print("Failed to select record into match table {}".format(error))
    except co.Error as error:
        print("Failed to connect :".format(error))
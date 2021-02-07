
# import platform
#
# def init():
#     platform.system()
#     if platform.system() == "Windows":
#         import psycopg2 as psy
#     else:
#         # import psycopg2-binary as psy
#         print("ok")
#
#     return psy
#
# def get_match():
#     psy = init()
#     """ insert a new vendor into the vendors table """
#     sql = """SELECT * FROM match;"""
#     conn = None
#     id = None
#     try:
#         # read database configuration
#
#         # connect to the PostgreSQL database
#         conn = psy.connect(user="postgres",
#                                   password="Jjci3kJy57b4GAsLWiUC",
#                                   host="db-1.ctjpvwq07ek9.us-east-2.rds.amazonaws.com",
#                                   port="5432",
#                                   database="postgres")
#         # create a new cursor
#         cur = conn.cursor()
#         # execute the INSERT statement
#         cur.execute(sql)
#         # commit the changes to the database
#         matchs = cur.fetchall()
#         # close communication with the database
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             return matchs
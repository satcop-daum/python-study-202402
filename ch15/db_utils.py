import mysql.connector


################################################################################
def get_connection():
    try:
        connection = mysql.connector.connect(
            user="dy_user",
            password="dy_1234",
            host="localhost",
            port=43307,
            database="dy_system"
        )
        return connection

    except mysql.connector.Error as e:
        print(f"에러 발생: {e}")

#end-def
################################################################################

def close_connection(connection):
    cursor = None
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.close()
            connection.close()

    except mysql.connector.Error as e:
        print(f"에러 발생: {e}")
#end-def
################################################################################


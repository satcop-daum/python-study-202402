import mysql.connector
from mysql.connector import Error

# MariaDB 접속 정보
config = {
    'host': 'localhost',         # 호스트
    'port': 43307,                # 포트 (기본 3306)
    'user': 'dysystem_user',     # MariaDB 사용자
    'password': 'dysystem_1234', # 비밀번호
    'database': 'dysystem'  # 사용할 DB
}

################################################################################
def get_connection():

    try:
        # 1. DB 연결
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            return connection

    except Error as e:
        print("오류 발생:", e)

    finally:
        print("MariaDB 연결 종료")

#end-def
################################################################################

def close_connection(connection):
    cursor = None
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.close()

    except Error as e:
        print("오류 발생:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MariaDB 연결 종료")
#end-def
################################################################################
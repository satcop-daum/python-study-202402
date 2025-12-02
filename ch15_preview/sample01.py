from datetime import datetime

from ch15_preview.db_utils import get_connection, close_connection

def action1():
    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
                   INSERT INTO bbs (title, content, create_date)
                   VALUES (%s, %s, NOW()) 
                   """

    title = '제목입니다. ' + str(datetime.now())
    contents = '내용입니다. ' + str(datetime.now())
    data = (title, contents)
    cursor.execute(insert_query, data)
    connection.commit()

    close_connection(connection)
# end-def
################################################################################

action1()

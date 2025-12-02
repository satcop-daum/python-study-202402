from datetime import datetime

from ch15.db_utils import get_connection
from ch15_preview.db_utils import close_connection

connection = get_connection()
cursor = connection.cursor()

title = '[파이썬추가] 제목입니다. ' + str(datetime.now())
contents = '[파이썬추가] 내용입니다. ' + str(datetime.now())

cursor.execute(
    "INSERT INTO bbs (title, content, create_time) VALUES (%s, %s, NOW())",
    (title, contents)
)
connection.commit()

close_connection(connection)

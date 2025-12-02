

import schedule
import time
import subprocess

def job():
    print('작업실행!!!', time.ctime())
    subprocess.run(["python", "db_test.py"])

#1분마다 실행
schedule.every(1).minutes.do(job)
# schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    #time.sleep(60)  # 1분마다 확인
    time.sleep(1)  # 1초마다 실행 대기

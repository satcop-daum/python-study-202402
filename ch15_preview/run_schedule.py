# pip install schedule
import schedule
import time
import subprocess

def job():
    print('실행!')
    subprocess.run(["python3", "./sample01.py"])

# schedule.every().day.at("09:00").do(job)

# 매 1분마다 실행
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

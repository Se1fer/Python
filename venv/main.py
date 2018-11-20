import itchat
from apscheduler.schedulers.background import BlockingScheduler
import datetime

def loginCallback():
    print("***登录成功***")
def sendExcel():
    name = 'VIP'
    iRoom = itchat.search_chatrooms(name)
    userName = ''
    for room in iRoom:
        if room['NickName'] == name:
            userName = room['UserName']
            break;
    fileDir = 'C:\\publish\\xm\\20181112.xlsx';
    itchat.send_file(fileDir, userName);

def exitCallback():
    print("***已退出***")

itchat.auto_login();
itchat.get_chatrooms(update=True)
date_value = (datetime.datetime.now()+ datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S");
scheduler = BlockingScheduler();
scheduler.add_job(sendExcel,'cron', day_of_week='mon-sun', hour=6, minute=10);
scheduler.start()



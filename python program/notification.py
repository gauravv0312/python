import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
        title="Please Drink Water Now !",
        message='Water is very important thing like life Because water is another name of life',
        app_icon="E:\python\notification\icon",
        timeout=2
    )
    time.sleep(6)   #put the time that you want to show again and again
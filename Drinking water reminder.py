# drinking water reminder

import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="PLEASE DRINK WATER....",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            # app_icon="C:\Users\it care\PycharmProjects\pythonProject1\icon.ico",  #for your icon
            timeout=5
        )
        time.sleep(10)

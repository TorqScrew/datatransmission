import datetime
import time
import gspread as gs

jsonfile = "datatele-366319-0d5fecc26b48.json"
gc = gs.service_account(jsonfile)

tp = gc.open("Tele2")
wk = tp.get_worksheet(4)
# for i in range(1,4):
#     for j in range(1,4):
#         wk.update_cell(i, j, str(datetime.datetime.now().time()))
#     time.sleep(0.5)
#wk.update_cell(1,1,"Eureka!!!")
# wk.close()
def col3(i):
    for j in range(1,4,1):
        wk.update_cell(i, j, str(datetime.datetime.now().time()))
        time.sleep(0.5)
    # for j in range(4):
    #     print(i)
    #     time.sleep(2)

def col2(i):
    for j in range(1,4,1):
        wk.update_cell(i, j, str(datetime.datetime.now().time()))
        time.sleep(0.5)
    # for j in range(4):
    #     print(i)
    #     time.sleep(2)

def col1(i):
    for j in range(1,4,1):
        wk.update_cell(i, j, str(datetime.datetime.now().time()))
        time.sleep(0.5)
    # for j in range(4):
    #     print(i)
    #     time.sleep(2)
col1(1)
col2(2)
col3(3)
print("hehe")
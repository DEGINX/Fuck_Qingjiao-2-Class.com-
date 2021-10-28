# Author: Bilibili@JonyanDunh(1309634881@qq.com) && Hanbings(3219065882@qq.com) && F_Unction(3593329288@qq.com)
# ___________             __     ________  .__                   __.__
# \_   _____/_ __   ____ |  | __ \_____  \ |__| ____    ____    |__|__|____    ____
#  |    __)|  |  \_/ ___\|  |/ /  /  / \  \|  |/    \  / ___\   |  |  \__  \  /  _ \
#  |     \ |  |  /\  \___|    <  /   \_/.  \  |   |  \/ /_/  >  |  |  |/ __ \(  <_> )
#  \___  / |____/  \___  >__|_ \ \_____\ \_/__|___|  /\___  /\__|  |__(____  /\____/
#      \/              \/     \/        \__>       \//_____/\______|       \/

import http.client
import re
import xlrd  # 导入库
import random

taskNum = 0
taskBigNum = 0
taskContestNum = 0


def Function(account, password):
    reqtoken, sid = Get_Cookies()
    Login(account, password, reqtoken, sid)
    Start3(reqtoken, sid)


def Login(account, password, reqtoken, sid):
    conn = http.client.HTTPSConnection("www.2-class.com")
    payload = "{\"account\":\"" + account + "\",\"password\":\"" + password + "\",\"checkCode\":\"\"," \
                                                                              "\"codeKey\":\"\",\"reqtoken\":\"" + \
              reqtoken + "\"} "
    headers = {
        'Host': 'www.2-class.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.75 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'https://www.2-class.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.2-class.com/courses',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'sid=' + sid
    }
    conn.request("POST", "/api/user/login", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))


def Get_Cookies():
    conn = http.client.HTTPSConnection("www.2-class.com")
    payload = ''
    headers = {}
    conn.request("GET", "/courses", payload, headers)
    res = conn.getresponse()
    data = res.read()
    sid = re.findall(r"sid=(.+?);", res.getheader("Set-Cookie"))[0]
    reqtoken = re.findall(r"reqtoken:\"(.+?)\"", data.decode("utf-8"))[0]
    return reqtoken, sid


def Compelete_Task(payload, sid):
    conn = http.client.HTTPSConnection("www.2-class.com")
    payload = payload
    headers = {
        'Host': ' www.2-class.com',
        'Connection': ' keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.75 Safari/537.36',
        'Content-Type': ' application/json;charset=UTF-8',
        'Accept': ' */*',
        'Origin': ' https://www.2-class.com',
        'Sec-Fetch-Site': ' same-origin',
        'Sec-Fetch-Mode': ' cors',
        'Sec-Fetch-Dest': ' empty',
        'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh;q=0.9',
        'Cookie': 'sid=' + sid
    }
    conn.request("POST", "/api/exam/commit", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    if "\"success\":true" in data.decode("utf-8"):
        global taskNum
        taskNum += 1

def Compelete_Final_Task(reqtoken, sid):
    conn = http.client.HTTPSConnection("2-class.com")
    payload = "{\"list\":[{\"questionId\":691,\"questionContent\":\"D\"},{\"questionId\":692,"\
              "\"questionContent\":\"D\"},{\"questionId\":693,\"questionContent\":\"C\"},{\"questionId\":694," \
              "\"questionContent\":\"B\"},{\"questionId\":695,\"questionContent\":\"D\"},{\"questionId\":696," \
              "\"questionContent\":\"D\"},{\"questionId\":697,\"questionContent\":\"B\"},{\"questionId\":698," \
              "\"questionContent\":\"C\"},{\"questionId\":699,\"questionContent\":\"C\"},{\"questionId\":700," \
              "\"questionContent\":\"B\"}],\"exam\":\"final\",\"reqtoken\":\"" + reqtoken + "\"}"
    headers = {
        'Host': ' 2-class.com',
        'Connection': ' keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.75 Safari/537.36',
        'Content-Type': ' application/json;charset=UTF-8',
        'Accept': ' */*',
        'Origin': ' https://2-class.com',
        'Sec-Fetch-Site': ' same-origin',
        'Sec-Fetch-Mode': ' cors',
        'Sec-Fetch-Dest': ' empty',
        'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh-HK;q=0.9,zh;q=0.8,en;q=0.7',
        'Cookie': ' sid=' + sid + ';'
    }
    conn.request("POST", "/api/question/commit", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    if "\"success\":true" in data.decode("utf-8"):
        global taskBigNum
        taskBigNum += 1


def Compelete_Contest_Task(reqtoken, sid):
    conn = http.client.HTTPSConnection("2-class.com")
    payload = "{\"list\":[{\"questionId\":2948,\"questionContent\":\"D\"},{\"questionId\":2949," \
              "\"questionContent\":\"B\"},{\"questionId\":2888,\"questionContent\":\"B\"},{\"questionId\":2889," \
              "\"questionContent\":\"D\"},{\"questionId\":2893,\"questionContent\":\"B\"},{\"questionId\":2957," \
              "\"questionContent\":\"D\"},{\"questionId\":2958,\"questionContent\":\"D\"},{\"questionId\":2895," \
              "\"questionContent\":\"A\"},{\"questionId\":2898,\"questionContent\":\"B\"},{\"questionId\":2963," \
              "\"questionContent\":\"A\"},{\"questionId\":2899,\"questionContent\":\"B\"},{\"questionId\":2932," \
              "\"questionContent\":\"D\"},{\"questionId\":2904,\"questionContent\":\"D\"},{\"questionId\":2969," \
              "\"questionContent\":\"A\"},{\"questionId\":2905,\"questionContent\":\"B\"},{\"questionId\":2906," \
              "\"questionContent\":\"B\"},{\"questionId\":2939,\"questionContent\":\"B\"},{\"questionId\":2909," \
              "\"questionContent\":\"A\"},{\"questionId\":2911,\"questionContent\":\"A\"},{\"questionId\":2912," \
              "\"questionContent\":\"B\"}],\"time\":281,\"reqtoken\":\"" + reqtoken + "\"} "
    headers = {
        'Host': ' 2-class.com',
        'Connection': ' keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.75 Safari/537.36',
        'Content-Type': ' application/json;charset=UTF-8',
        'Accept': ' */*',
        'Origin': ' https://2-class.com',
        'Sec-Fetch-Site': ' same-origin',
        'Sec-Fetch-Mode': ' cors',
        'Sec-Fetch-Dest': ' empty',
        'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh-HK;q=0.9,zh;q=0.8,en;q=0.7',
        'Cookie': ' sid=' + sid + ';'
    }
    conn.request("POST", "/api/quiz/commit", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    if "\"success\":true" in data.decode("utf-8"):
        global taskContestNum
        taskContestNum += 1


# 高一级
def Start1(reqtoken, sid):
    print(taskBigNum)
    print("payload已过期！")
    return
    print(
        "-----------------------------------------------------------" + sid + "-----------------------------------------------------------")
    payload = "{\"courseId\":\"837\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":\"0,2\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"838\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,1,2\"},{\"examId\":2," \
              "\"answer\":\"0,2\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"782\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":0},{\"examId\":2," \
              "\"answer\":0},{\"examId\":3,\"answer\":2},{\"examId\":4,\"answer\":1},{\"examId\":5,\"answer\":0}]," \
              "\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"779\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":1},{\"examId\":3,\"answer\":1},{\"examId\":4,\"answer\":3},{\"examId\":5,\"answer\":0}]," \
              "\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    Compelete_Final_Task(reqtoken, sid)
    # Compelete_Contest_Task(reqtoken, sid)
    print("\n")


# 高二级
def Start(reqtoken, sid):
    print(
        "-----------------------------------------------------------" + sid + "-----------------------------------------------------------")
    payload ="{\"courseId\":\"1113\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,1,3\"},{\"examId\":2," \
              "\"answer\":\"0,1,3\"}],\"reqtoken\":\"" +reqtoken + "\"}"
    Compelete_Task(payload, sid)

    payload = "{\"courseId\":\"1088\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":1},{\"examId\":2,"\
              "\"answer\":2}],\"reqtoken\":\"" + reqtoken + "\"}"
    Compelete_Task(payload, sid)

    '''
    payload = "{\"courseId\":\"835\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"1,2\"},{\"examId\":2," \
              "\"answer\":\"0,2,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)

    payload = "{\"courseId\":\"836\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":1},{\"examId\":2," \
              "\"answer\":2}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    '''

    Compelete_Final_Task(reqtoken, sid)
    Compelete_Contest_Task(reqtoken, sid)
    print("\n")



# 五年级
def Start3(reqtoken, sid):
    print("payload已过期！")
    return
    print(
        "-----------------------------------------------------------" + sid + "-----------------------------------------------------------")
    payload = "{\"courseId\":\"848\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,1,3\"},{\"examId\":2," \
              "\"answer\":\"0,1,2,4\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"829\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":0},{\"examId\":2," \
              "\"answer\":\"0,1,3\"},{\"examId\":3,\"answer\":\"0,1,2\"}],\"exam\":\"course\"," \
              "\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"825\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":0},{\"examId\":2," \
              "\"answer\":2},{\"examId\":3,\"answer\":2},{\"examId\":4,\"answer\":3},{\"examId\":5,\"answer\":\"0,1," \
              "2,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"826\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":3},{\"examId\":3,\"answer\":1},{\"examId\":4,\"answer\":1},{\"examId\":5,\"answer\":\"0," \
              "2\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"773\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":2},{\"examId\":3,\"answer\":0},{\"examId\":4,\"answer\":2},{\"examId\":5,\"answer\":3}]," \
              "\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"847\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"2,3\"},{\"examId\":2," \
              "\"answer\":\"0,1,3\"},{\"examId\":3,\"answer\":\"0,1,2\"}],\"exam\":\"course\"," \
              "\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    Compelete_Final_Task(reqtoken, sid)
    Compelete_Contest_Task(reqtoken, sid)
    print("\n")
    
# 初三
def Start9(reqtoken, sid):
    print("payload已过期！")
    return
    print(
        "-----------------------------------------------------------" + sid + "-----------------------------------------------------------")
    payload = "{\"courseId\":\"861\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,1,2\"},{\"examId\":2,\"answer\":\"0,1,2,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"839\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,1,3\"},{\"examId\":2,\"answer\":\"1,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"840\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"1,2\"},{\"examId\":2,\"answer\":\"0,1,2,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"768\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,1\"},{\"examId\":2,\"answer\":2},{\"examId\":3,\"answer\":\"0,1,2,3\"},{\"examId\":4,\"answer\":\"0,1,2,3\"},{\"examId\":5,\"answer\":3}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"767\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2,\"answer\":0},{\"examId\":3,\"answer\":0},{\"examId\":4,\"answer\":0},{\"examId\":5,\"answer\":1}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    Compelete_Final_Task(reqtoken, sid)
    Compelete_Contest_Task(reqtoken, sid)
    print("\n")

# 初一
def Start4(reqtoken, sid):
    print("payload已过期！")
    return
    print(
        "-----------------------------------------------------------" + sid + "-----------------------------------------------------------")
    payload = "{\"courseId\":\"859\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":0},{\"examId\":2,\"answer\":\"0,1,2\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"}"
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"844\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,2\"},{\"examId\":2,\"answer\":\"0,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"}"
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"843\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2,\"answer\":\"0,1,2\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"}"
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"771\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":3},{\"examId\":2,\"answer\":2},{\"examId\":3,\"answer\":1},{\"examId\":4,\"answer\":3},{\"examId\":5,\"answer\":1}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"}"
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"772\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2,\"answer\":3},{\"examId\":3,\"answer\":0},{\"examId\":4,\"answer\":0},{\"examId\":5,\"answer\":\"0,1\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"}"
    Compelete_Task(payload, sid)
    #############################################
    payload = "{\"courseId\":\"848\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"0,1,3\"},{\"examId\":2," \
              "\"answer\":\"0,1,2,4\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"829\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":0},{\"examId\":2," \
              "\"answer\":\"0,1,3\"},{\"examId\":3,\"answer\":\"0,1,2\"}],\"exam\":\"course\"," \
              "\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"825\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":0},{\"examId\":2," \
              "\"answer\":2},{\"examId\":3,\"answer\":2},{\"examId\":4,\"answer\":3},{\"examId\":5,\"answer\":\"0,1," \
              "2,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"826\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":3},{\"examId\":3,\"answer\":1},{\"examId\":4,\"answer\":1},{\"examId\":5,\"answer\":\"0," \
              "2\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"773\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":2},{\"examId\":3,\"answer\":0},{\"examId\":4,\"answer\":2},{\"examId\":5,\"answer\":3}]," \
              "\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"847\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"2,3\"},{\"examId\":2," \
              "\"answer\":\"0,1,3\"},{\"examId\":3,\"answer\":\"0,1,2\"}],\"exam\":\"course\"," \
              "\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    Compelete_Final_Task(reqtoken, sid)
    Compelete_Contest_Task(reqtoken, sid)
    print("\n")


def B():
    global taskNum
    global taskBigNum
    print("\033[34m")
    print(" ___________             __     ________  .__                   __.__")
    print(" \\_   _____/_ __   ____ |  | __ \\_____  \\ |__| ____    ____    |__|__|____    ____")
    print("  |    __)|  |  \\_/ ___\\|  |/ /  /  / \\  \\|  |/    \\  / ___\\   |  |  \\__  \\  /  _ \\")
    print("|     \\ |  |  /\\  \\___|    <  /   \\_/.  \\  |   |  \\/ /_/  >  |  |  |/ __ \\(  <_> )")
    print("  \\___  / |____/  \\___  >__|_ \\ \\_____\\ \\_/__|___|  /\\___  /\\__|  |__(____  /\\____/")
    print("      \\/              \\/     \\/        \\__>       \\//_____/\\______|       \\/")
    print("\033[33m")
    print("共完成普通试题: " + str(taskNum) + "份 " + "共完成考试试题: " + str(taskBigNum) + "份")
    print("顺利完成了" + str(taskContestNum) + "个账号的任务 \n")
    print("作者: Bilibili@JonyanDunh(1309634881@qq.com) && Hanbings(3219065882@qq.com) && F_Unction(3593329288@qq.com)")
    print("Author: Bilibili@JonyanDunh(1309634881@qq.com) && Hanbings(3219065882@qq.com) && F_Unction(3593329288@qq.com)\n")
    print("如果被抓 务必铭记 不然网站管理员就不知道为什么全国的题都在一个IP做的了 ：）")
    print("\033[0m")


def Piliang():
    xlsx = xlrd.open_workbook("./Student_Qingjiao_List.xls")
    sheet1 = xlsx.sheets()[0]
    i = 0
    while i < sheet1.nrows:
        # Random=random.randint(0,1900);
        Function(sheet1.row_values(i)[0], str(sheet1.row_values(i)[1])[0:8])
        i += 1


Piliang()
B()

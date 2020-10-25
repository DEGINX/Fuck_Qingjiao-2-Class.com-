# Author: Bilibili@JonyanDunh(1309634881@qq.com) && Hanbings(3219065882@qq.com)
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
    Start(reqtoken, sid)


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
    payload = "{\"list\":[{\"questionId\":677,\"questionContent\":\"A\"},{\"questionId\":678," \
              "\"questionContent\":\"A\"},{\"questionId\":679,\"questionContent\":\"B\"},{\"questionId\":680," \
              "\"questionContent\":\"D\"},{\"questionId\":681,\"questionContent\":\"A\"},{\"questionId\":682," \
              "\"questionContent\":\"B\"},{\"questionId\":683,\"questionContent\":\"A\"},{\"questionId\":684," \
              "\"questionContent\":\"C\"},{\"questionId\":685,\"questionContent\":\"C\"},{\"questionId\":686," \
              "\"questionContent\":\"A\"}],\"exam\":\"final\",\"reqtoken\":\"" + reqtoken + "\"} "
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
    Random=random.randint(0,6)
    if Random==0:#100分
        payload = "{\"list\":[{\"questionId\":2744,\"questionContent\":\"B\"},{\"questionId\":2681," \
              "\"questionContent\":\"C\"},{\"questionId\":2745,\"questionContent\":\"B\"},{\"questionId\":2682," \
              "\"questionContent\":\"A\"},{\"questionId\":2685,\"questionContent\":\"A\"},{\"questionId\":2687," \
              "\"questionContent\":\"D\"},{\"questionId\":2753,\"questionContent\":\"D\"},{\"questionId\":2755," \
              "\"questionContent\":\"A\"},{\"questionId\":2692,\"questionContent\":\"B\"},{\"questionId\":2757," \
              "\"questionContent\":\"A\"},{\"questionId\":2693,\"questionContent\":\"C\"},{\"questionId\":2760," \
              "\"questionContent\":\"A\"},{\"questionId\":2761,\"questionContent\":\"A\"},{\"questionId\":2762," \
              "\"questionContent\":\"B\"},{\"questionId\":2699,\"questionContent\":\"D\"},{\"questionId\":2700," \
              "\"questionContent\":\"A\"},{\"questionId\":2705,\"questionContent\":\"D\"},{\"questionId\":2706," \
              "\"questionContent\":\"A\"},{\"questionId\":2770,\"questionContent\":\"B\"},{\"questionId\":2771," \
              "\"questionContent\":\"A\"}],\"time\":281,\"reqtoken\":\"" + reqtoken + "\"} "
    elif Random==1:#95分
        payload = "{\"list\":[{\"questionId\":2744,\"questionContent\":\"B\"},{\"questionId\":2681," \
                  "\"questionContent\":\"A\"},{\"questionId\":2745,\"questionContent\":\"B\"},{\"questionId\":2682," \
                  "\"questionContent\":\"A\"},{\"questionId\":2685,\"questionContent\":\"A\"},{\"questionId\":2687," \
                  "\"questionContent\":\"D\"},{\"questionId\":2753,\"questionContent\":\"D\"},{\"questionId\":2755," \
                  "\"questionContent\":\"A\"},{\"questionId\":2692,\"questionContent\":\"B\"},{\"questionId\":2757," \
                  "\"questionContent\":\"A\"},{\"questionId\":2693,\"questionContent\":\"C\"},{\"questionId\":2760," \
                  "\"questionContent\":\"A\"},{\"questionId\":2761,\"questionContent\":\"A\"},{\"questionId\":2762," \
                  "\"questionContent\":\"B\"},{\"questionId\":2699,\"questionContent\":\"D\"},{\"questionId\":2700," \
                  "\"questionContent\":\"A\"},{\"questionId\":2705,\"questionContent\":\"D\"},{\"questionId\":2706," \
                  "\"questionContent\":\"A\"},{\"questionId\":2770,\"questionContent\":\"B\"},{\"questionId\":2771," \
                  "\"questionContent\":\"A\"}],\"time\":281,\"reqtoken\":\"" + reqtoken + "\"} "
    elif Random==2:#90分
        payload = "{\"list\":[{\"questionId\":2744,\"questionContent\":\"B\"},{\"questionId\":2681," \
                  "\"questionContent\":\"A\"},{\"questionId\":2745,\"questionContent\":\"B\"},{\"questionId\":2682," \
                  "\"questionContent\":\"A\"},{\"questionId\":2685,\"questionContent\":\"A\"},{\"questionId\":2687," \
                  "\"questionContent\":\"A\"},{\"questionId\":2753,\"questionContent\":\"D\"},{\"questionId\":2755," \
                  "\"questionContent\":\"A\"},{\"questionId\":2692,\"questionContent\":\"B\"},{\"questionId\":2757," \
                  "\"questionContent\":\"A\"},{\"questionId\":2693,\"questionContent\":\"C\"},{\"questionId\":2760," \
                  "\"questionContent\":\"A\"},{\"questionId\":2761,\"questionContent\":\"A\"},{\"questionId\":2762," \
                  "\"questionContent\":\"B\"},{\"questionId\":2699,\"questionContent\":\"D\"},{\"questionId\":2700," \
                  "\"questionContent\":\"A\"},{\"questionId\":2705,\"questionContent\":\"D\"},{\"questionId\":2706," \
                  "\"questionContent\":\"A\"},{\"questionId\":2770,\"questionContent\":\"B\"},{\"questionId\":2771," \
                  "\"questionContent\":\"A\"}],\"time\":281,\"reqtoken\":\"" + reqtoken + "\"} "
    elif Random == 3 or Random == 4:#85分
        payload = "{\"list\":[{\"questionId\":2744,\"questionContent\":\"B\"},{\"questionId\":2681," \
                  "\"questionContent\":\"A\"},{\"questionId\":2745,\"questionContent\":\"B\"},{\"questionId\":2682," \
                  "\"questionContent\":\"A\"},{\"questionId\":2685,\"questionContent\":\"A\"},{\"questionId\":2687," \
                  "\"questionContent\":\"A\"},{\"questionId\":2753,\"questionContent\":\"D\"},{\"questionId\":2755," \
                  "\"questionContent\":\"A\"},{\"questionId\":2692,\"questionContent\":\"B\"},{\"questionId\":2757," \
                  "\"questionContent\":\"A\"},{\"questionId\":2693,\"questionContent\":\"C\"},{\"questionId\":2760," \
                  "\"questionContent\":\"A\"},{\"questionId\":2761,\"questionContent\":\"A\"},{\"questionId\":2762," \
                  "\"questionContent\":\"A\"},{\"questionId\":2699,\"questionContent\":\"D\"},{\"questionId\":2700," \
                  "\"questionContent\":\"A\"},{\"questionId\":2705,\"questionContent\":\"D\"},{\"questionId\":2706," \
                  "\"questionContent\":\"A\"},{\"questionId\":2770,\"questionContent\":\"B\"},{\"questionId\":2771," \
                  "\"questionContent\":\"A\"}],\"time\":281,\"reqtoken\":\"" + reqtoken + "\"} "
    elif Random == 5:  # 80分
        payload = "{\"list\":[{\"questionId\":2744,\"questionContent\":\"B\"},{\"questionId\":2681," \
                  "\"questionContent\":\"A\"},{\"questionId\":2745,\"questionContent\":\"A\"},{\"questionId\":2682," \
                  "\"questionContent\":\"A\"},{\"questionId\":2685,\"questionContent\":\"A\"},{\"questionId\":2687," \
                  "\"questionContent\":\"A\"},{\"questionId\":2753,\"questionContent\":\"D\"},{\"questionId\":2755," \
                  "\"questionContent\":\"A\"},{\"questionId\":2692,\"questionContent\":\"B\"},{\"questionId\":2757," \
                  "\"questionContent\":\"A\"},{\"questionId\":2693,\"questionContent\":\"C\"},{\"questionId\":2760," \
                  "\"questionContent\":\"A\"},{\"questionId\":2761,\"questionContent\":\"A\"},{\"questionId\":2762," \
                  "\"questionContent\":\"A\"},{\"questionId\":2699,\"questionContent\":\"D\"},{\"questionId\":2700," \
                  "\"questionContent\":\"A\"},{\"questionId\":2705,\"questionContent\":\"D\"},{\"questionId\":2706," \
                  "\"questionContent\":\"A\"},{\"questionId\":2770,\"questionContent\":\"B\"},{\"questionId\":2771," \
                  "\"questionContent\":\"A\"}],\"time\":281,\"reqtoken\":\"" + reqtoken + "\"} "
    elif Random == 6:  # 75分
        payload = "{\"list\":[{\"questionId\":2744,\"questionContent\":\"B\"},{\"questionId\":2681," \
                  "\"questionContent\":\"A\"},{\"questionId\":2745,\"questionContent\":\"A\"},{\"questionId\":2682," \
                  "\"questionContent\":\"A\"},{\"questionId\":2685,\"questionContent\":\"A\"},{\"questionId\":2687," \
                  "\"questionContent\":\"A\"},{\"questionId\":2753,\"questionContent\":\"A\"},{\"questionId\":2755," \
                  "\"questionContent\":\"A\"},{\"questionId\":2692,\"questionContent\":\"B\"},{\"questionId\":2757," \
                  "\"questionContent\":\"A\"},{\"questionId\":2693,\"questionContent\":\"C\"},{\"questionId\":2760," \
                  "\"questionContent\":\"A\"},{\"questionId\":2761,\"questionContent\":\"A\"},{\"questionId\":2762," \
                  "\"questionContent\":\"A\"},{\"questionId\":2699,\"questionContent\":\"D\"},{\"questionId\":2700," \
                  "\"questionContent\":\"A\"},{\"questionId\":2705,\"questionContent\":\"D\"},{\"questionId\":2706," \
                  "\"questionContent\":\"A\"},{\"questionId\":2770,\"questionContent\":\"B\"},{\"questionId\":2771," \
                  "\"questionContent\":\"A\"}],\"time\":281,\"reqtoken\":\"" + reqtoken + "\"} "
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


def Start(reqtoken, sid):
    print(
        "-----------------------------------------------------------" + sid + "-----------------------------------------------------------")
    payload = "{\"courseId\":\"781\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":2},{\"examId\":3,\"answer\":1},{\"examId\":4,\"answer\":2},{\"examId\":5,\"answer\":3}]," \
              "\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"780\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2," \
              "\"answer\":0},{\"examId\":3,\"answer\":1},{\"examId\":4,\"answer\":2},{\"examId\":5,\"answer\":\"0,1," \
              "2\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"835\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":\"1,2\"},{\"examId\":2," \
              "\"answer\":\"0,2,3\"}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
    Compelete_Task(payload, sid)
    payload = "{\"courseId\":\"836\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":1},{\"examId\":2," \
              "\"answer\":2}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"} "
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
    print("作者: Bilibili@JonyanDunh(1309634881@qq.com) && Hanbings(3219065882@qq.com)")
    print("Author: Bilibili@JonyanDunh(1309634881@qq.com) && Hanbings(3219065882@qq.com)\n")
    print("如果被抓 务必铭记 不然网站管理员就不知道为什么全国的题都在一个IP做的了 ：）")
    print("\033[0m")


def Piliang():
    xlsx = xlrd.open_workbook("./Student_Qingjiao_List.xlsx")
    sheet1 = xlsx.sheets()[0]
    i = 0
    while i < sheet1.nrows:
        Function(sheet1.row_values(i)[0], str(sheet1.row_values(i)[1])[0:8])
        i += 1


Piliang()
B()

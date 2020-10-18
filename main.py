#Author: Bilibili@JonyanDunh(1309634881@qq.com) && Hanbings(3219065882@qq.com)
import http.client
import re
def Get_Cookies():
  conn = http.client.HTTPSConnection("www.2-class.com")
  payload = ''
  headers = {}
  conn.request("GET", "/courses", payload, headers)
  res = conn.getresponse()
  data = res.read()
  sid = re.findall(r"sid=(.+?);", res.getheader("Set-Cookie"))[0]
  reqtoken = re.findall(r"reqtoken:\"(.+?)\"", data.decode("utf-8"))[0]
  print(reqtoken)
  print(sid)
  return reqtoken,sid
def Login(account,password,reqtoken,sid):
  conn = http.client.HTTPSConnection("www.2-class.com")
  payload = "{\"account\":\""+account+"\",\"password\":\""+password+"\",\"checkCode\":\"\",\"codeKey\":\"\",\"reqtoken\":\"" + reqtoken + "\"}"
  headers = {
    'Host': 'www.2-class.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
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
  print(data.decode("utf-8"))
def Compelete_Task(payload,sid):
  conn = http.client.HTTPSConnection("www.2-class.com")
  payload = payload
  headers = {
    'Host': ' www.2-class.com',
    'Connection': ' keep-alive',
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Content-Type': ' application/json;charset=UTF-8',
    'Accept': ' */*',
    'Origin': ' https://www.2-class.com',
    'Sec-Fetch-Site': ' same-origin',
    'Sec-Fetch-Mode': ' cors',
    'Sec-Fetch-Dest': ' empty',
    'Referer': ' https://www.2-class.com/courses/exams/781',
    'Accept-Encoding': ' gzip, deflate, br',
    'Accept-Language': ' zh-CN,zh;q=0.9',
    'Cookie': 'sid=' + sid
  }
  conn.request("POST", "/api/exam/commit", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))

reqtoken,sid=Get_Cookies()

Login("dengjunyuan595","56216359",reqtoken,sid)
payload = "{\"courseId\":\"781\",\"examCommitReqDataList\":[{\"examId\":1,\"answer\":2},{\"examId\":2,\"answer\":2},{\"examId\":3,\"answer\":1},{\"examId\":4,\"answer\":2},{\"examId\":5,\"answer\":3}],\"exam\":\"course\",\"reqtoken\":\"" + reqtoken + "\"}"
Compelete_Task(payload,sid)



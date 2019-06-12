#!/usr/bin/python
#-*-coding:utf-8-*-
import requests,json

url="http://pts.linkcld.com:9040/gzcx-space-server/index/getModuleList"
headers ={
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8"
}
params= {
         "h":{"deviceId":"fixedDeviceID",
              "userToken":"",
              "appCode":"330921",
              "codeValue":"3309",
              "sourceCodeValue":"330921",
              "appVersion":"1.0.0",
              "deviceTypeName":"ios"},
        "b":{"type":"1",
               "moduleType":"0",
               "create_time":"1542786780000"}
              }
r=requests.post(url,data=json.dumps(params),headers=headers)
print(r.text)


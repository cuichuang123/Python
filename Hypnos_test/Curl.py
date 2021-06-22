import requests
from string import Template
from Hypnos_test.request_data import *

haders = {'Content-Type': 'application/json'}
url='http://127.0.0.1:8082/chatbot/echo.bot'
post_data = {
  "event": {
    "header": {
      "tenantId": 62,
      "requestId": "ac74d5d8cc47836deaee0b8d8b7250cc",
      "type": 1,
      "createTime": 1610197536,
      "actionMode": 1,
      "serializeType": "Json",
      "ctx": {
        "bizChatType": "consult",
        "mainAccNick": "teatap"
      }
    },
    "body": {
      "ext": {
        "messageTag": "consult-msg"
      },
      "bizUniqueId": "1662f732-2837-4cde-a5cb-cb3a2a34b7e6",
      "msgId": "6269468287837448442",
      "channelType": "bc",
      "content": "{\"text\":\"====\"}",
      "messageType": "NONE_SYS",
      "createTime": 1610197536,
      "sender": {
        "nick": "cuichuang2014",
        "domain": "cntaobao"
      },
      "receivers": [
        {
          "nick": "teatap:服务助手",
          "domain": "cntaobao"
        }
      ],
      "contentType": 1
    }
  },
  "clusterTest": "false",
  "runTestCase": "true",
  "chatRequestTimeMillis": 1607412960606
}

class Requst_curl:
    def request_data(self,str):
        text = Template('"{\\"text\\":\\" ${s2} \\"}"')
        content = text.safe_substitute(s2=str)
        #   json.loads()用于将str类型的数据转成dict
        content_list = json.loads(content)
        # post_data:接口发送的请求
        post_data['event']['body']['content'] = content_list

        print(post_data)
        # json.dumps() 转化为json格式 将dict类型的数据转成str
        res = requests.post(url, headers=haders, data=json.dumps(post_data))
        # print(res.status_code)
        response = json.loads(res.text)
        # response
        # return response
        print(response)


if __name__ == '__main__':
    req = Requst_curl()
    req.request_data('今天下雨了')
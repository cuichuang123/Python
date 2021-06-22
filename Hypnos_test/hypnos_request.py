import time
from Hypnos_test.hypons_Reply import *
from Hypnos_test.hypnos_to_human import *
from Hypnos_test.hypnos_no_answer import *

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

# str ='吊牌剪了能不能退'

lists = ['吊牌剪了能不能退','包装要一起退回吗','退款原因写什么']
# 正常回复场景： 吊牌剪了能不能退
# 无答案场景：包装要一起退回吗
# 转人工场景:退款原因写什么

class Request:

  # 验证接口返回的数据和数据中的数据是否一致
  def request_reply(self,str):
    reply = HypnosReply()
    reply.reply_content(str)

  # 查看发送的请求场景的答案是否为无答案
  def request_noanswer(self,str):
    reply = HypnosNoanswer()
    reply.noanswer_content(str)

  # 查看发送的请求的配置是否为转人工
  def  request_tohuman(self,str):
    reply = HypnosToHuman()
    reply.tohuman_content(str)


if __name__ == '__main__':
    req = Request()
    for str in lists:
      if str == '吊牌剪了能不能退':
         req.request_reply(str)
         # time.sleep(60)
      elif str == '包装要一起退回吗':
         req.request_noanswer(str)
      else:
         req.request_tohuman(str)


'''
# 将返回的数据转化为字典的格式
  res1 =response['value'][0]['body']['content']
  res2 = json.loads(res1)
# 定位到接口返回的数据
  print(res2['templateData']['text'])
'''

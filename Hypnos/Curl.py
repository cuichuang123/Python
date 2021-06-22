import requests
import json
import uuid
import time

from string import Template
from Hypnos.Request_Node import NodeMysql
from Hypnos.Request_Catalog import CatalogMysql



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
      "bizUniqueId": "99af7cc6-28ac-412c-b20f-31ff07a39563",
      "msgId": "6269468287837448442",
      "channelType": "bc",
      "content": "{\"text\":\"====\"}",
      "messageType": "NONE_SYS",
      "createTime": 1615283355000,
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
  "chatRequestTimeMillis": 1607412960606
}

bizUniqueId = str(uuid.uuid4())

class Requst_curl:
  '''
  发送cur请求
  '''
  def request_data(self, str):
    # 传入参数，拼接起来

    text = Template('"{\\"text\\":\\"${s2}\\"}"')
    content = text.safe_substitute(s2=str)
    #   json.loads()用于将str类型的数据转成list
    content_list = json.loads(content)

    # post_data:接口发送的请求
    post_data['event']['body']['bizUniqueId'] = bizUniqueId
    print(bizUniqueId)
    post_data['event']['body']['content'] = content_list

    # print(post_data)
    # json.dumps() 转化为json格式 将dict类型的数据转成str
    res = requests.post(url, headers=haders, data=json.dumps(post_data))
    response = res.text
    return response

  # 查询节点库数据
  def Nodedata(self,biz):
    print(bizUniqueId + '+++++++++++')
    nodelog = NodeMysql()
    res = nodelog.answer_data("SELECT content FROM chat_message WHERE user_id = 1 and `receive_qimen_msg_biz_uniq_id` = '"+biz+"' ORDER BY `dx_created` DESC;")
    print(res)

  # 查询web库数据
  def Catalogdata(self):
    catalog = CatalogMysql()
    res = catalog.answer_data("SELECT answer_contents FROM `faq_custom_scene` fcs JOIN `faq_answer_config` fac on fcs.`id` = fac.`faq_scene_id`   WHERE fcs.`user_id` =1 and fcs.name = '这个场景不要删除';")
    data = json.loads(str(res).strip("('',)"))
    one_data =   str(data[0]['contents']).strip("['']")  # 这个答案也不要修改删除哦亲～～～
    print(one_data)

if __name__ == '__main__':
  req = Requst_curl()
  req.request_data('不要删除亲')
  # 因为是接口返回的数据是异步的，所以需要等待几秒钟，才能调用接口返回的数据
  time.sleep(3)
  req.Nodedata(bizUniqueId)
  req.Catalogdata()

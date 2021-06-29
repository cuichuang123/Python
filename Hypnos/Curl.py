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
        "nick": "北音执念5",
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



class Requst_curl:
  '''
  发送cur请求
  '''


  def request_data(self,param,bizUniqueId):
    # 传入参数，拼接起来
    print(param)
    text = Template('"{\\"text\\":\\"${s2}\\"}"')
    content = text.safe_substitute(s2=param)
    #   json.loads()用于将str类型的数据转成list
    content_list = json.loads(content)
    # post_data:接口发送的请求
    post_data['event']['body']['bizUniqueId'] = bizUniqueId
    post_data['event']['body']['content'] = content_list

    # json.dumps() 转化为json格式 将dict类型的数据转成str
    res = requests.post(url, headers=haders, data=json.dumps(post_data))
    response = res.text
    print(response)
    return response

  # # # 查询节点库数据
  # def Nodedata(self,biz):
  #   nodelog = NodeMysql()
  #   # 注意返回的结果中：可能带有欢迎语
  #   res = nodelog.answer_data("SELECT content FROM chat_message WHERE user_id = 1 and `receive_qimen_msg_biz_uniq_id` = '"+biz+"' and direction=0 ORDER BY `dx_created` DESC;")
  #   # 注意返回的结果中：可能带有欢迎语,带有欢迎语时会解析失败
  #   res_data = str(res).strip("(('',),)")
  #   print(res_data)
  #   return res_data
  #
  # # 查询web库数据
  # def Catalogdata(self,cj_name):
  #   catalog = CatalogMysql()
  #   res = catalog.answer_data("SELECT answer_contents FROM `faq_custom_scene` fcs JOIN `faq_answer_config` fac on fcs.`id` = fac.`faq_scene_id`   WHERE fcs.name = '"+cj_name+"'  and fcs.`user_id` =1 ;")
  #   data = json.loads(str(res).strip("('',)"))
  #   one_data =  str(data[0]['contents']).strip("['']")  # 这个答案也不要修改删除哦亲～～～
  #   print(one_data)
  #   return one_data
  #
  # # 判断返回的数据跟web库配置的数据是否一致
  # def Eaquls_node_catalog(self):
  #    node_data = self.Nodedata(bizUniqueId)
  #    cata_data = self.Catalogdata(cj_name)
  #    if node_data == cata_data:
  #      print("接口返回的数据跟配置的数据一致")
  #    else:
  #      print("啥也不是")

if __name__ == '__main__':
  pass
  # req = Requst_curl()
  # cj_shili = '不要修改亲'
  # cj_name = '这个场景不要删除'
  # req.request_data(cj_shili)
  # # 因为是接口返回的数据是异步的，所以需要等待几秒钟，才能调用接口返回的数据
  # time.sleep(3)
  # req.Nodedata(bizUniqueId)
  # req.Catalogdata(cj_name)
  # req.Eaquls_node_catalog()


from Hypnos_test.Curl import *

# 调用ConneMysql方法
one_mysql = ConnectMysql()
res1 = one_mysql.answer_data('SELECT fac.`content`  FROM `faq_scene_release` fsr JOIN `faq_answer_config` fac on fsr.`faq_scene_id`  = fac.`faq_scene_id` WHERE fsr.`name`= "消费者询问退换货要求" and fac.`user_id`= 1  GROUP BY fsr.`faq_scene_id` ')
sql_data = one_mysql.split_data(res1)



class HypnosReply:
    def reply_content(self,str):
       res = Requst_curl()
       response = res.request_data(str)
       # 将返回的数据转化为字典的格式
       res1 = response['value'][0]['body']['content']
       res2 = json.loads(res1)
       Interface_data = res2['templateData']['text']
       # print('1、数据库查询数据：', sql_data)
       # print("1、接口返回的数据：",Interface_data)
       if sql_data == Interface_data:
           print("1、普通场景Case：通过")
       else:
           print("1、普通场景Case：不通过")


if __name__ == '__main__':
    reply = HypnosReply()
    # reply.reply_content()



'''
接口返回的格式：
{'success': True, 'code': 0, 'message': None, 'value': [{'header': {'tenantId': 62, 'requestId': 
'ac74d5d8cc47836deaee0b8d8b7250cc', 'type': 1, 'createTime': 1610197536, 'actionMode': 1, 
'serializeType': 'Json', 'ctx': {'bizChatType': 'consult', 'mainAccNick': 'teatap'}}, 
'body': {'createTime': 1615534720817, 'bizUniqueId': 'ba96452b-51b8-4a3c-a4ea-8ce8e2358425', 
'ext': None, 'msgId': None, 'sender': {'domain': 'cntaobao', 'nick': 'teatap:服务助手'}, 
'receivers': [{'domain': 'cntaobao', 'nick': 'cuichuang2014'}], 'contentType': 1, 
'content': '{"templateId":"1593403771864","templateData":{"text":"不动就不动呗"}}', 
'channelType': 'bc'}}]}
'''


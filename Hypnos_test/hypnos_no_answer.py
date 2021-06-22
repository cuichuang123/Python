from Hypnos_test.Curl import *
from Hypnos_test.request_data import *

one_mysql = ConnectMysql()
# 查询该场景有没有开启开关
res1 = one_mysql.answer_data("select active from faq_scene_user_config fs  join faq_scene_release fr on fs.`faq_scene_id` = fr.`faq_scene_id` where fr.name = '消费者询问退货邮寄的注意事项' and fs.user_id = 1 group by fr.name;")
sql_data = one_mysql.split_data(res1)
active = int(sql_data)

# 查询无答案策略配置话术
res2 = one_mysql.answer_data("SELECT no_answer_default_reply_content FROM `user_reception_config` where `user_id`  = 1 ;")
no_answer_content = one_mysql.split_data(res2)
# print(no_answer_content)
class HypnosNoanswer:
    def noanswer_content(self,str):
        res = Requst_curl()
        response = res.request_data(str)
        # 将返回的数据转化为字典的格式
        res1 = response['value'][0]['body']['content']
        res2 = json.loads(res1)
        Interface_data = res2['templateData']['text']
        # print('2、该场景是否开启：', active)
        # print("2、接口返回的数据：", Interface_data)
        if active == 0 :
            if no_answer_content == Interface_data:
                print("2、走无答案Case：通过")
            else:
                print("2、走无答案Case：失败")
                print('2、接口返回数据：',Interface_data)
                print('2、数据查询数据：',no_answer_content)
        else:
            print('2、该场景已被激活，请查看该场景配置是否被修改')


if __name__ == '__main__':
    reply = HypnosNoanswer()
    # reply.noanswer_content()


'''
{'success': True, 'code': 0, 'message': None, 'value': [{'header': {'tenantId': 62, 
'requestId': 'ac74d5d8cc47836deaee0b8d8b7250cc', 'type': 1, 'createTime': 1610197536,
 'actionMode': 1, 'serializeType': 'Json', 'ctx': {'bizChatType': 'consult', 'mainAccNick': 
 'teatap'}}, 'body': {'createTime': 1615534781670, 'bizUniqueId': 'f8b65a10-074c-41d6-aee0-0e06bf053c15',
  'ext': None, 'msgId': None, 'sender': {'domain': 'cntaobao', 'nick': 'teatap:服务助手'}, 
  'receivers': [{'domain': 'cntaobao', 'nick': 'cuichuang2014'}], 'contentType': 1,
   'content': '{"templateId":"1593403771864","templateData":{"text":"抱歉ss，1是个机器人，还在学习中，暂时无法解决您的这个问题，您可以再换个问题问问我。ss"}}', 
   'channelType': 'bc'}}]}
'''
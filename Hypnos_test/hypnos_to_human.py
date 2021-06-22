from Hypnos_test.Curl import *

# 调用ConneMysql方法
one_mysql = ConnectMysql()
# 查询回复类型是否为转人工
res1 = one_mysql.answer_data("SELECT reply_type FROM `faq_scene_release` fsr JOIN `faq_answer_config` fac on fsr.`faq_scene_id`  = fac.`faq_scene_id`  WHERE fsr.`name`= '消费者询问退款申请时原因如何选择'   and fac.`user_id`= 1  GROUP BY fsr.`faq_scene_id`  = 77")
sql_data = one_mysql.split_data(res1)

# 查询转接引导话术
res2 = one_mysql.answer_data("SELECT transfer_guide_words FROM `user_reception_config` where `user_id`  = 1 ;")
transfer_content = one_mysql.split_data(res2)
# print(transfer_content)

class HypnosToHuman:
    def tohuman_content(self,str):
        res = Requst_curl()
        response = res.request_data(str)
        # 定位转接引导话术
        res = response['value'][0]['body']['content']
        res1 = json.loads(res)
        Interface1_data = res1['templateData']['text']
        # 定位转接失败话术
        res2 =  response['value'][1]['body']['ext']
        res3 = json.loads(json.dumps(res2))
        Interface2_data = res3['transfer_failed_desc']
        if sql_data == 'TRANS_TO_HUMAN':
            if transfer_content == Interface1_data:
                print("3、转接人工Case：通过")
            else:
                print('3、转接人工Case：不通过')
                print('3、接口返回数据：', Interface1_data)
                print('3、数据查询数据：', sql_data)
        else:
            print('3、该场景答案配置的不是转接人工服务')



if __name__ == '__main__':
    reply = HypnosToHuman()
    # reply.tohuman_content()


'''
{'success': True, 'code': 0, 'message': None, 'value': [{'header': {'tenantId': 62, 
'requestId': 'ac74d5d8cc47836deaee0b8d8b7250cc', 'type': 1, 'createTime': 1610197536,
 'actionMode': 1, 'serializeType': 'Json', 'ctx': {'bizChatType': 'consult', 'mainAccNick': 'teatap'}},
  'body': {'createTime': 1615535934405, 'bizUniqueId': '853368b7-e860-41c8-af57-8b014f995d90', 
  'ext': None, 'msgId': None, 'sender': {'domain': 'cntaobao', 'nick': 'teatap:服务助手'},
   'receivers': [{'domain': 'cntaobao', 'nick': 'cuichuang2014'}], 'contentType': 1, 
   'content': '{"templateId":"1593403771864","templateData":{"text":"马上马上就好"}}', 
   'channelType': 'bc'}}, {'header': {'tenantId': 62, 'requestId': 'ac74d5d8cc47836deaee0b8d8b7250cc', 
   'type': 3, 'createTime': 1610197536, 'actionMode': 1, 'serializeType': 'Json', 'ctx': {'bizChatType': 'consult', 
   'mainAccNick': 'teatap'}}, 'body': {'createTime': 1610197536, 'bizUniqueId': '1662f732-2837-4cde-a5cb-cb3a2a34b7e6',
    'ext': {'messageTag': 'consult-msg', 'transfer_failed_desc': '抱歉，转接失败ss'}, 
    'msgId': '6269468287837448442', 'sender': {'domain': 'cntaobao', 'nick': 'cuichuang2014'},
     'receivers': [{'domain': 'cntaobao', 'nick': 'teatap:服务助手'}], 'contentType': 1, 
     'content': '{"text":" 场景不能动哦 "}', 'channelType': 'bc'}}]}

'''
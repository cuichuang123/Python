import time


from Hypnos.Run_Main import bizUniqueId
from Hypnos.Curl import *
from Hypnos.Request_Node import *
from Hypnos.Request_Catalog import *



class Hypnos_Reply:

    # 查询节点库数据
    def Nodedata(self, biz):
        nodelog = NodeMysql()
        # 注意返回的结果中：可能带有欢迎语
        res = nodelog.answer_data("SELECT content FROM chat_message WHERE user_id = 1 and `receive_qimen_msg_biz_uniq_id` = '" + biz + "' and direction=0 ORDER BY `dx_created` DESC;")
        # 注意返回的结果中：可能带有欢迎语,带有欢迎语时会解析失败
        res_data = str(res).strip("(('',),)")
        return res_data

    # 查询web库数据
    def Catalogdata(self, cj_name):
        catalog = CatalogMysql()
        res = catalog.answer_data("SELECT answer_contents FROM `faq_custom_scene` fcs JOIN `faq_answer_config` fac on fcs.`id` = fac.`faq_scene_id`   WHERE fcs.name = '" + cj_name + "'  and fcs.`user_id` =1 ;")
        data = json.loads(str(res).strip("('',)"))
        one_data = str(data[0]['contents']).strip("['']")  # 这个答案也不要修改删除哦亲～～～
        return one_data

    # 判断返回的数据跟web库配置的数据是否一致
    def Eaquls_node_catalog(self,cj_name):
        node_data = self.Nodedata(bizUniqueId)
        cata_data = self.Catalogdata(cj_name)
        if node_data == cata_data:
            print("接口返回的数据跟配置的数据一致")
        else:
            print("啥也不是")

    def Run_reply(self):
        cj_shili = '不要修改亲'
        cj_name = '这个场景不要删除'
        res = Requst_curl()
        res.request_data(cj_shili, bizUniqueId)
        reply = Hypnos_Reply()
        # 因为是接口返回的数据是异步的，所以需要等待几秒钟，才能调用接口返回的数据
        time.sleep(3)
        reply.Nodedata(bizUniqueId)
        reply.Catalogdata(cj_name)
        reply.Eaquls_node_catalog(cj_name)


if __name__ == '__main__':
    pass
    # cj_shili = '不要修改亲'
    # cj_name = '这个场景不要删除'
    # res = Requst_curl()
    # res.request_data(cj_shili,bizUniqueId)
    # reply = Hypnos_Reply()
    # # 因为是接口返回的数据是异步的，所以需要等待几秒钟，才能调用接口返回的数据
    # time.sleep(3)
    # reply.Nodedata(bizUniqueId)
    # reply.Catalogdata(cj_name)
    # reply.Eaquls_node_catalog()
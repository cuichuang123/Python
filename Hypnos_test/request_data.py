import pymysql
import json

class ConnectMysql:
    '''
    # 打开数据库
    db = pymysql.connect("localhost","testuser","test123","testDB")
    # 使用cursor（）方法创建游标cursor
    cursor = db.cursor()
    # 使用execute（）方法执行sql查询
    cursor.execute（"select * from 。。。"）
    '''
    def __init__(self):
        # 创建一个连接数据的对象
        self.cont = pymysql.connect(
            host= '192.168.100.12',
            user= 'darcy',
            passwd='TsRAScf1aTojt1',
            port= 3306,
            charset='utf8',
            db= 'hypnos_catalog2'
        )
        self.cur = self.cont.cursor()

    # 查询数据
    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    # 解析teatap所有的场景示例
    def Examples_txt(self,result):
        with open('sql_data.txt','w') as f:
            sql_data = json.loads(json.dumps(result))
            list_data = []
            for data in sql_data:
                str_data = str(data)
                # print(str_data)
                # 将数据拆分截取
                str_data1 = str_data.strip("['']")
                # print(str_data1)
                # print(str_data1.split('/')[0])
                split_data = str_data1.split('/')[0]
                # print(type(split_data))
                list_data.append(split_data)
            # print(list_data)
            return list_data


    # 执行sql，返回sql的数据
    def answer_data(self,sql):
        self.cur.execute(sql)
        result_data = self.cur.fetchone()
        return result_data


    # 解析sql返回的数据
    def split_data(self,result):
        data = str(json.loads(json.dumps(result)))
        sql_data = data.strip("['']")
        return sql_data


if __name__ == '__main__':
    one_mysql = ConnectMysql()
    # 查询单个用户所有的场景示例
    # res = one_mysql.search_one('SELECT fsr.`instance` FROM `faq_scene_release` fsr JOIN `faq_scene` fs on fsr.`intent_id`= fs.`scene_code` JOIN `faq_scene_user_config` fsuc on fs.`id` = fsuc.`faq_scene_id` WHERE fsuc.`user_id`  = 1 GROUP BY fs.`scene_code` ')
    # one_mysql.Examples_txt(res)
    # 查询单个场景的答案sql
    # res1 = one_mysql.answer_data('SELECT fac.`content`  FROM `faq_scene_release` fsr JOIN `faq_answer_config` fac on fsr.`faq_scene_id`  = fac.`faq_scene_id` WHERE fsr.`name`= "消费者询问退换货要求" and fac.`user_id`= 1  GROUP BY fsr.`faq_scene_id`  = 75')
    # one_mysql.split_data(res1)
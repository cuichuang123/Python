import pymysql

class NodeMysql:
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
            user= '**',
            passwd='***',
            port= 3306,
            charset='utf8',
            db= 'hypnos_node'
        )
        # 创建游标
        self.cur = self.cont.cursor()

    # 执行sql，返回sql的数据
    def answer_data(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

if __name__ == '__main__':
    nodelog = NodeMysql()
    # 查询单个用户所有的场景示例
    # res = one_mysql.search_all('SELECT fsr.`instance` FROM `faq_scene_release` fsr JOIN `faq_scene` fs on fsr.`intent_id`= fs.`scene_code` JOIN `faq_scene_user_config` fsuc on fs.`id` = fsuc.`faq_scene_id` WHERE fsuc.`user_id`  = 1 GROUP BY fs.`scene_code` ')
    # one_mysql.Examples_txt(res)
    # 查询单个场景的答案sql
    # res1 = catalog.answer_data( 'SELECT content FROM chat_message WHERE user_id = 1 and `receive_qimen_msg_biz_uniq_id` = "379ba2cd-a1dd-400f-9881-6747ceb891c3" ORDER BY `dx_created` DESC')
    # print(res1)




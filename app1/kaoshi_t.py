import pymysql
import random


class KaoShiClass(object):

    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="dsq171007", port=3306, database="bysj")
        self.cursor = self.db.cursor()
        self.t = []

    def get_ti(self):
        self.cursor.execute("select * from app1_tiku_xzt")
        self.db.commit()
        self.t = random.sample(self.cursor.fetchall(), 10)
        return self.t

    def set_KaoShi_db(self, kaoshi_id, ti):
        for t in ti:
            print(f"insert into app1_tikuguanli(key_KaoShi_b_id, key_TiKu_a_id) values ({str(kaoshi_id)}, {str(t[0])})")
            self.cursor.execute(f"insert into app1_tikuguanli(key_KaoShi_b_id, key_TiKu_a_id) values ({str(kaoshi_id)}, {str(t[0])})")
            self.db.commit()


if __name__ == '__main__':
    kaoshi = KaoShiClass()
    ti = kaoshi.get_ti()
    kaoshi.set_KaoShi_db(4, ti)


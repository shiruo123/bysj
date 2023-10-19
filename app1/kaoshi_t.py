import pymysql
import random


class KaoShiClass(object):

    def __init__(self):
        self.db = pymysql.connect(host="119.29.244.36", user="youthrefuel", password="dsq171007", port=3306, database="bysj")
        self.cursor = self.db.cursor()
        self.t = []
        random.seed(1)

    def input(self, i):
        if i == 1:
            self.t1()
        elif i == 2:
            self.t2()
        elif i == 3:
            self.t3()
        elif i == 4:
            self.t4()

    def t1(self):
        self.cursor.execute("select * from app1_tiku_xzt")
        self.db.commit()
        self.t = random.sample(self.cursor.fetchall(), 10)

    def t2(self):
        self.cursor.execute("select * from app1_tiku_pdt")
        self.db.commit()
        self.t = random.sample(self.cursor.fetchall(), 10)

    def t3(self):
        self.cursor.execute("select * from app1_tiku_xzt")
        self.db.commit()
        ti1 = random.sample(self.cursor.fetchall(), 5)
        self.cursor.execute("select * from app1_tiku_pdt")
        self.db.commit()
        ti2 = random.sample(self.cursor.fetchall(), 5)
        self.t = ti1 + ti2

    def t4(self):
        self.cursor.execute("select * from app1_tiku_xzt1")
        self.db.commit()
        self.t = self.cursor.fetchall()

    def text(self):
        return self.t


if __name__ == '__main__':
    kaoshi = KaoShiClass()
    kaoshi.t4()
    print(kaoshi.text())

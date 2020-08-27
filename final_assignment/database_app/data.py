import mysql.connector


class Database():
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',user='root', password='sanjaya',database='final_assignment')
        self.cur = self.connection.cursor()

    def add(self,query,values):
        self.cur.execute(query, values)
        self.connection.commit()

    def delete(self,query,values):
        self.cur.execute(query, values)
        self.connection.commit()

    def update(self,query, values):
        self.cur.execute(query, values)
        self.connection.commit()

    def select(self,query):
        self.cur.execute(query)
        res = self.cur.fetchall()
        self.connection.commit()
        return res

    def selectvalue(self,query,value):
        self.cur.execute(query,value)
        res = self.cur.fetchall()
        self.connection.commit()
        return res


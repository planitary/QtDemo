# coding:gbk
import pymysql
import hashlib
from Config import DbConfig
class LoginController:

    UserToken = ''
    # ״̬�ֶΣ����ڷ����жϵ�¼״̬
    isPwd = False                       # �û�����
    isUserName = False                      # ���������ƥ��

    def __init__(self,user,pwd):
        self.user = user
        self.password = pwd

    @classmethod
    def __DbInit(cls):
        db_dict = {'name': DbConfig.user,
                   'pwd': DbConfig.password,
                   'port': DbConfig.port,
                   'db': DbConfig.db,
                   'charset': DbConfig.charset,
                   'host': DbConfig.host}
        # ���ݿ�ê��,�������쳣�ഫ�����ݿ�����
        cursor = 1
        # �������ݿ�
        conn = pymysql.connect(host=db_dict['host'], user=db_dict['name'], password=db_dict['pwd'],
                               db=db_dict['db'], charset=db_dict['charset'])
        return conn

    def Login(self):
        db = self.__DbInit()
        cur = db.cursor()
        user = self.user
        pwd_ = self.password
        # user = 'login'
        # pwd_ = '12345'
        hashPwd = hashlib.md5()
        hashPwd.update(pwd_.encode('utf8'))
        pwd = hashPwd.hexdigest()
        checkUserByNameAndPwdSql = "select * from users where name = '%s'" % user
        cur.execute(checkUserByNameAndPwdSql)
        findResult = cur.fetchone()
        # print(findResult[3])
        # �ҵ����û����ж�����
        if findResult is not None:
            self.isUserName = True
            if pwd == findResult[3]:
                self.isPwd = True
            else:
                self.isPwd = False
        else:
            self.isUserName = False

    def getStatus(self):
        return self.isUserName,self.isPwd


# if __name__ == "__main__":
#     s = LoginController()
#     s.Login()




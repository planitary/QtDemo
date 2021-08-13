# coding:gbk
import pymysql
import hashlib
from Config import DbConfig
from Extra.CreateToken import Token
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
        # print(pwd)
        checkUserByNameAndPwdSql = "select name,password from users where name = '%s'" % user
        cur.execute(checkUserByNameAndPwdSql)
        findResult = cur.fetchone()
        # print(findResult[3])
        # �ҵ����û����ж�����
        if findResult is not None:
            self.isUserName = True
            if pwd == findResult[1]:
                self.isPwd = True
            else:
                self.isPwd = False
        else:
            self.isUserName = False

    def getStatus(self):
        return self.isUserName,self.isPwd

class RegController:
    userToken = ''
    regOk = False
    def __init__(self,username,pwd,phone):
        self.username = username
        self.password = pwd
        self.phone = phone
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

    def Register(self):
        conn = self.__DbInit()
        cur = conn.cursor()
        self.userToken = Token().getToken(self.username)
        findInfoByUserNameSql = "select name from users where name = '%s'" % self.username
        cur.execute(findInfoByUserNameSql)
        userResult = cur.fetchone()
        # �ҵ����û���Ϣ�����û�������
        if userResult is not None:
            self.regOk = False
        else :
            insertUserInfoSql = "insert into users (name,password,token,phoneNumber) " \
                                "VALUES ('%s',md5('%s'),'%s','%s')" % (self.username,self.password,self.userToken,self.phone)
            cur.execute(insertUserInfoSql)
            conn.commit()
            self.regOk = True

    def getStatus(self):
        return self.regOk

# if __name__ == "__main__":
#     s = LoginController()
#     s.Login()

import hashlib,base64
class UserService():
    
    # 结合salt和md5 生成加密的密码
    @staticmethod
    def generatePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode("utf-8")),salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()
    
    # 对Cookie中存储的信息进行加密
    @staticmethod
    def generateAuthCode(user_info = None):
        m = hashlib.md5()
        str = "%s-%s-%s-%s"%(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

import hashlib

class Token():
    def _CreateToken(self,name):
        constStr = 'QT'
        _userToken_ = constStr + name
        Serialize = hashlib.sha1()
        Serialize.update(_userToken_.encode('utf8'))
        return Serialize.hexdigest()

    def getToken(self,name):
        self._userToken = self._CreateToken(name)
        return self._userToken

if __name__ == '__main__':
    ex = Token()
    print(ex.getToken('jack'))

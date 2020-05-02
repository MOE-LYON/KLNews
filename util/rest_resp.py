
class Resp(object):

    def __init__(self,data=None,code = 200,msg = "success"):
        self.data = data
        self.code = code
        self.msg = msg
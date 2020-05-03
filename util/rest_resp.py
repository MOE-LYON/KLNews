
class Resp(dict):

    def __init__(self, data=None, code=200, msg="success"):
        super().__init__()
        self['data'] = data
        self['code'] = code
        self['msg'] = msg
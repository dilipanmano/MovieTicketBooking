import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or b'\xde\x17\xad\t\x16\xa5K\x9c\xa9=\x1c$\xe9\xa1\x14\xce'
    
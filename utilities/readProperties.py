import configparser

import config

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        email=config.get('common info','email')
        return email
    @staticmethod
    def getUserpassword():
        password=config.get('common info','password')
        return password

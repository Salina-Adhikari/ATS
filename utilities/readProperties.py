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

    @staticmethod
    def getPhoto():
        photo=config.get('user info','photo')
        return photo
    @staticmethod
    def getUsername():
        username=config.get('user info','username')
        return username
    @staticmethod
    def getEmail():
        u_email=config.get('user info','useremail')
        return u_email
    @staticmethod
    def getPhonenummber():
        phone=config.get('user info','phonenumber')
        return phone
    @staticmethod
    def getPassword():
        password=config.get('user info','password')
        return password
    @staticmethod
    def getRoles():
        roles=config.get('user info','setroles')
        return roles

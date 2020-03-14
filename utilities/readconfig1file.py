import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\config1.ini")
class Getinfoconfig:
    @staticmethod
    def wedurlget():
        Weburl=config.get("common info","Weburl")
        return  Weburl

    @staticmethod
    def usernameget():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def passwordget():
        password = config.get("common info", "password")
        return password
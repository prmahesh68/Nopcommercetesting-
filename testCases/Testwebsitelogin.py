from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readconfig1file import Getinfoconfig
from utilities.CustomLogger import Logsetup
import pytest
import time

class Test_001:
    Weburl = Getinfoconfig.wedurlget()
    username = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()
    # Openbrowser = webdriver.Chrome()
    # Loginobject = Login(Openbrowser)
    logger = Logsetup.getlog()

    def testtitle(self,web):
        self.logger.info("starting Title test")
        self.Openbrowser = web
        self.logger.info("Opening browser")
        self.Openbrowser.get(self.Weburl)
        self.logger.info("Opening website")
        Title =self.Openbrowser.title
        self.logger.info("checking title")
        # self.Openbrowser.close()
        if Title == "Your store. Login":
            self.Openbrowser.close()
            return True
        else:
            self.Openbrowser.save_screenshot(".//Screenshots/Noptesttitle.png")
            self.logger.info("saving error screenshot")
            self.Openbrowser.close()
            assert False


    def testlogin(self,web):
        self.logger.info("starting Login test")
        self.Openbrowser = web
        self.logger.info("starting browser")
        Loginobject = Login(self.Openbrowser)
        self.logger.info("starting browser")
        self.Openbrowser.get(self.Weburl)
        Loginobject.setusername(self.username)
        Loginobject.setpassword(self.password)
        Loginobject.clicklogin()
        time.sleep(5)
        Title=self.Openbrowser.title
        self.logger.info("checking title after login")

        if Title=="Dashboard / nopCommerce administration":
            self.Openbrowser.close()
            assert True==True
        else:
            self.Openbrowser.save_screenshot(".//Screenshots/Nop_testlogin.png")
            self.logger.info("Saving screenshot")
            self.Openbrowser.close()
            assert False





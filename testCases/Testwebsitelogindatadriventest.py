from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readconfig1file import Getinfoconfig
from utilities.CustomLogger import Logsetup
from utilities import xlutils
import pytest
import time

class Test_002_datadriventest:
    Weburl = Getinfoconfig.wedurlget()
    datapath = ".//TestData/ecommerce test data.xlsx"
     # Openbrowser = webdriver.Chrome()
    # Loginobject = Login(Openbrowser)
    logger = Logsetup.getlog()
    status_list=[]

    # def testtitle(self,web):
    #     self.logger.info("starting Title test")
    #     self.Openbrowser = web
    #     self.logger.info("Opening browser")
    #     self.Openbrowser.get(self.Weburl)
    #     self.logger.info("Opening website")
    #     Title =self.Openbrowser.title
    #     self.logger.info("checking title")
    #     # self.Openbrowser.close()
    #     if Title == "Your store. Login":
    #         self.Openbrowser.close()
    #         return True
    #     else:
    #         self.Openbrowser.save_screenshot(".//Screenshots/Noptesttitle.png")
    #         self.logger.info("saving error screenshot")
    #         self.Openbrowser.close()
    #         assert False


    def testlogindatadriventest(self,web):
        self.logger.info("starting Login test")
        self.Openbrowser = web
        self.logger.info("starting browser")
        Loginobject = Login(self.Openbrowser)
        self.logger.info("starting browser")
        self.Openbrowser.get(self.Weburl)
        self.row =xlutils.getrowcount(self.datapath,'Sheet1')
        self.column =xlutils.getcolumnount(self.datapath,'Sheet1')
        for row in range(2,self.row+1):
            self.username=xlutils.readfromxl(self.datapath,'Sheet1',row,1)
            self.password=xlutils.readfromxl(self.datapath,'Sheet1',row,2)
            self.expectedresult=xlutils.readfromxl(self.datapath, 'Sheet1', row, 3)
            print(self.username,self.password,self.expectedresult)
            Loginobject.setusername(self.username)
            Loginobject.setpassword(self.password)
            Loginobject.clicklogin()
            time.sleep(5)
            Title=self.Openbrowser.title
            Act_tile= "Dashboard / nopCommerce administration"
            self.logger.info("checking title after login")
            if Title== Act_tile:
                if self.expectedresult=="pass":
                    self.logger.info("This test passed")
                    self.status_list.append("pass")
                    Loginobject.clicklogout()
                elif self.expectedresult=="fail":
                    self.logger.info("This test passed")
                    self.status_list.append("fail")
                    Loginobject.clicklogout()
            elif Title != Act_tile:
                if self.expectedresult == "fail":
                    self.logger.info("This test passed")
                    self.status_list.append("pass")
                    print(self.status_list)
                elif self.expectedresult=="pass":
                    self.logger.info("This test passed")
                    self.status_list.append("fail")
        print(self.status_list)
        if "fail" not in self.status_list:
            print ("Overall test case passed")
            self.logger.info("Overall test passed")
            self.Openbrowser.close()
            assert True
        else:
            print("overall test failed")
            self.logger.info("Overall test failed")
            self.Openbrowser.close()
            assert False





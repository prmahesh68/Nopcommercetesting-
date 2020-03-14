from selenium import webdriver
import time
import datetime
from datetime import date,datetime
from pageObjects.LoginPage import Login
from pageObjects.addcustomer import Addcust
from utilities.readconfig1file import Getinfoconfig
from utilities.CustomLogger import Logsetup
from utilities import xlutils

class Test_004:
    Weburl = Getinfoconfig.wedurlget()
    username = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()
    logger = Logsetup.getlogadd()
    datapath=".//TestData//addcustomerinnop.xlsx"

    def testaddcustomer(self, web):
        self.Openbrowser = web
        Loginobject = Login(self.Openbrowser)
        self.Openbrowser.get(self.Weburl)
        self.logger.info("starting browser")
        self.Openbrowser.maximize_window()
        Loginobject.setusername(self.username)
        Loginobject.setpassword(self.password)
        Loginobject.clicklogin()
        self.logger.info("Login completed")
        self.row = xlutils.getrowcount(self.datapath, 'Sheet1')
        self.column = xlutils.getcolumnount(self.datapath, 'Sheet1')
        Addnewcust = Addcust(self.Openbrowser)
        Addnewcust.customermenuclick()
        self.pass_status=[]
        for row in range(2, self.row + 1):
            self.email = xlutils.readfromxl(self.datapath, 'Sheet1', row, 1)
            self.custpassword = xlutils.readfromxl(self.datapath, 'Sheet1', row, 2)
            self.firstname = xlutils.readfromxl(self.datapath, 'Sheet1', row, 3)
            self.lastname = xlutils.readfromxl(self.datapath, 'Sheet1', row, 4)
            self.gender = xlutils.readfromxl(self.datapath, 'Sheet1', row, 5)
            self.DOB = xlutils.readfromxl(self.datapath, 'Sheet1', row, 6)
            self.companyname = xlutils.readfromxl(self.datapath, 'Sheet1', row, 7)
            self.istaxexempt = xlutils.readfromxl(self.datapath, 'Sheet1', row, 8)
            self.yourstorename = xlutils.readfromxl(self.datapath, 'Sheet1', row, 9)
            self.teststore2 = xlutils.readfromxl(self.datapath, 'Sheet1', row, 10)
            self.customerrole = xlutils.readfromxl(self.datapath, 'Sheet1', row, 11)
            self.vendor= xlutils.readfromxl(self.datapath, 'Sheet1', row, 12)
            self.active = xlutils.readfromxl(self.datapath, 'Sheet1', row, 13)
            self.admincomment = xlutils.readfromxl(self.datapath, 'Sheet1', row, 14)
            time.sleep(3)
            Addnewcust.customersubmenuclick()
            self.logger.info("Customer page opening")
            time.sleep(3)
            Addnewcust.addnewclick()
            self.logger.info("Customer second page opening")
            time.sleep(3)
            Addnewcust.emailinput(self.email)
            Addnewcust.passwordinput(self.custpassword)
            Addnewcust.firstnameinput(self.firstname)
            Addnewcust.genderselect(self.gender)
            Addnewcust.lastnameinput(self.lastname)
            Addnewcust.dateofbirthinput(self.DOB)
            Addnewcust.companynameinput(self.companyname)
            Addnewcust.newletter1input(self.yourstorename)
            Addnewcust.newsletter2input(self.teststore2)
            Addnewcust.customerroleselection(self.customerrole)
            Addnewcust.vendortypeselect(self.vendor)
            Addnewcust.admincomment(self.admincomment)
            self.logger.info("All Input to the add page done")
            Addnewcust.savecustomer()
            message=self.Openbrowser.find_element_by_tag_name("body").text
            if "The new customer has been added successfully." in message:
                self.pass_status.append("Pass")
            else:
                self.pass_status.append("Fail")
        print(self.pass_status)
        if "Fail" not in self.pass_status:
            self.logger.info("All test passed")
            assert True
        else:
            self.logger.info("All/Some of the test failed")
            assert False










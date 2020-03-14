from selenium import webdriver
from selenium.webdriver.support.ui import Select
from utilities.dateconverter import Date_spilt

class Addcust:
    link_customer_menu_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    link_customer_submenu_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    button_add_new_xpath = "/html[1]/body[1]/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    textbox_email_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    textbox_firstname_xpath="//input[@id='FirstName']"
    textbox_lastname_xpath="//input[@id='LastName']"
    radio_male_xpath="//input[@id='Gender_Male']"
    radio_female_xpath="//input[@id='Gender_Female']"
    datapicker_DOB_xpath="//input[@id='DateOfBirth']"
    textbox_company_xpath="//input[@id='Company']"
    tickmark_taxexempt_xpath="//input[@id='IsTaxExempt']"
    tickmark_newletter_store_xpath="//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div[1]/label/input"
    tickmark_newsletter_teststore="//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div[2]/label/input"
    selectbox_customerrole_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    selectrole_administator_xpath = "//li[contains(text(),'Administrators')]"
    selectrole_forummoderator_xpath="//li[contains(text(),'Forum Moderators')]"
    selectrole_guest_xpath="//li[contains(text(),'Guests')]"
    selectrole_registered_xpath = "//li[contains(text(),'Registered')]"
    deselectrole_registered_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[2]"
    deselectrole_adminstrator_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li[2]/span[2]"
    selectrole_vendor_xpath = "//li[contains(text(),'Vendors')]"
    dropdown_vendor_xpath="//select[@id='VendorId']"
    tickmark_active_xpath ="//input[@id='Active']"
    textbod_admincomments_xpath="//textarea[@id='AdminComment']"
    button_save_name = "save"

    def __init__(self, Openbrowser):
        self.Openbrowser = Openbrowser


    def customermenuclick(self):
        self.Openbrowser.find_element_by_xpath(self.link_customer_menu_xpath).click()
    def customersubmenuclick(self):
        self.Openbrowser.find_element_by_xpath(self.link_customer_submenu_xpath).click()
    def addnewclick(self):
        self.Openbrowser.find_element_by_xpath(self.button_add_new_xpath).click()
    def firstnameinput(self,firstname):
        self.Openbrowser.find_element_by_xpath(self.textbox_firstname_xpath).send_keys(firstname)
    def lastnameinput(self,lastname):
        self.Openbrowser.find_element_by_xpath(self.textbox_lastname_xpath).send_keys(lastname)
    def emailinput(self,email):
        self.Openbrowser.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)
    def passwordinput(self,custpassword):
        self.Openbrowser.find_element_by_xpath(self.textbox_password_xpath).send_keys(custpassword)
    def genderselect (self,gender):
        if gender == "male":
            self.Openbrowser.find_element_by_xpath(self.radio_male_xpath).click()
        elif gender == "female":
            self.Openbrowser.find_element_by_xpath(self.radio_female_xpath).click()
        else:
            self.Openbrowser.find_element_by_xpath(self.radio_male_xpath).click()
    def dateofbirthinput(self,DOB):
        dob= Date_spilt.dataconverter1(DOB)
        self.Openbrowser.find_element_by_xpath(self.datapicker_DOB_xpath).send_keys(dob)
    def companynameinput(self,companyname):
        self.Openbrowser.find_element_by_xpath(self.textbox_company_xpath).send_keys(companyname)
    def newletter1input(self,yourstorename):
        if yourstorename == "yes":
            self.Openbrowser.find_element_by_xpath(self.tickmark_newletter_store_xpath).click()
    def newsletter2input(self,teststore2):
        if teststore2 == "yes":
            self.Openbrowser.find_element_by_xpath(self.tickmark_newsletter_teststore).click()
    def customerroleselection(self, customerrole):
        customerolelist = customerrole.split(',')
        print(customerolelist)
        if "Guest" in customerolelist:
            self.Openbrowser.find_element_by_xpath(self.deselectrole_registered_xpath).click()
            # self.Openbrowser.find_element_by_xpath(self.selectrole_guest_xpath).click()
            role=self.Openbrowser.find_element_by_xpath(self.selectrole_guest_xpath)
            self.Openbrowser.execute_script("arguments[0].click();",role)
        else:
            if "Administrator" in customerolelist:
                role = self.Openbrowser.find_element_by_xpath(self.selectrole_administator_xpath)
                self.Openbrowser.execute_script("arguments[0].click();", role)
            if "Forum Moderators" in customerolelist:
                role = self.Openbrowser.find_element_by_xpath(self.selectrole_forummoderator_xpath)
                self.Openbrowser.execute_script("arguments[0].click();", role)
            if "Vendors" in customerolelist:
                if "Administrator" in customerolelist:
                    self.Openbrowser.find_element_by_xpath(self.deselectrole_adminstrator_xpath).click()
                role=self.Openbrowser.find_element_by_xpath(self.selectrole_vendor_xpath)
                self.Openbrowser.execute_script("arguments[0].click();", role)
            # self.Openbrowser.find_element_by_xpath(self.selectrole_forummoderator_xpath).click()
    def vendortypeselect (self,vendor):
        drop=Select(self.Openbrowser.find_element_by_xpath(self.dropdown_vendor_xpath))
        drop.select_by_visible_text(vendor)
    def selectactive(self,active):
        if active == "no":
            self.Openbrowser.find_element_by_path(self.tickmark_active_xpath).click()
    def admincomment(self,comments):
        self.Openbrowser.find_element_by_xpath(self.textbod_admincomments_xpath).send_keys(comments)
    def savecustomer(self):
        self.Openbrowser.find_element_by_name(self.button_save_name).click()







    
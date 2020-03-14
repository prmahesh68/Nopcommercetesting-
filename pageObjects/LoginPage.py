from selenium import webdriver

class Login:
    textbox_usernme_id="Email"
    textbox_password_id="Password"
    click_login_xpath="//input[@class='button-1 login-button']"
    click_logout_linktext="Logout"

    def __init__(self,Openbrowser):
        self.Openbrowser=Openbrowser
    def setusername(self,username):
        self.Openbrowser.find_element_by_id(self.textbox_usernme_id).clear()
        self.Openbrowser.find_element_by_id(self.textbox_usernme_id).send_keys(username)

    def setpassword(self, password):
        self.Openbrowser.find_element_by_id(self.textbox_password_id).clear()
        self.Openbrowser.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.Openbrowser.find_element_by_xpath(self.click_login_xpath).click()

    def clicklogout(self):
        self.Openbrowser.find_element_by_link_text(self.click_logout_linktext).click()

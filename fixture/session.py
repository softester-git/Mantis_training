from time import sleep

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, user_pass):
        wd = self.app.wd
        #self.app.open_main_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(user_name)
        wd.find_element_by_xpath("//input[@type='submit']").click()
        wd.find_element_by_name("password")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(user_pass)
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        sleep(1)
        wd.find_element_by_name("user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == "(%s)" % username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.label hidden-xs label-default arrowed").text

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

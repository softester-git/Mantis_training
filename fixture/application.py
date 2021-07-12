from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.support.select import Select
import os
import string
import random

class Application:

    def __init__(self, browser, baseurl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.baseurl = baseurl

    def open_main_page(self):
        wd = self.wd
        wd.get(self.baseurl)

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name)
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_fields(self, field_name, text):
        wd = self.wd
        if text is not None:
            if not field_name == "photo":
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).send_keys(os.path.abspath(text))

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        wd = self.wd
        try:
            self.wd.current_url
            return True
        except:
            return False

    def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def open_create_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[@href='/mantisbt-2.25.2/manage_overview_page.php']").click()
        wd.find_element_by_link_text(u"Управление проектами").click()
        wd.find_element_by_xpath("//button[@type='submit']").click()

    def fill_form(self, pname, pdesc):
        wd = self.wd
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(pname)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(pdesc)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()

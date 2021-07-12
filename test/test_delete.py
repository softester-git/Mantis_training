import random


def test_delete(app):
    wd = app.wd
    assert app.soap.can_login(username="administrator", password="admin")
    app.session.login(user_name="administrator", user_pass="admin")
    assert app.session.is_logged_in_as("administrator")
    #select projects to delete
    wd.find_element_by_xpath("//a[@href='/mantisbt-2.25.2/manage_overview_page.php']").click()
    wd.find_element_by_link_text(u"Управление проектами").click()
    tab = wd.find_element_by_css_selector("table")
    hrefs = tab.find_elements_by_css_selector("a")
    plist = []
    for i in hrefs:
        plist.append([i.text])
    pdel = list(random.choice(plist[5:]))
    wd.find_element_by_link_text(str(pdel)).click()
    wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
    wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
    # check deletion
    wd.find_element_by_xpath("//a[@href='/mantisbt-2.25.2/manage_overview_page.php']").click()
    wd.find_element_by_link_text(u"Управление проектами").click()
    tab = wd.find_element_by_css_selector("table")
    hrefs = tab.find_elements_by_css_selector("a")
    flag = 0
    for i in hrefs:
        if i.text == pdel:
            flag = 1
    assert flag != 1
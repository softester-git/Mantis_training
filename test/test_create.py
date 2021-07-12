def test_create(app):
    wd = app.wd
    assert app.soap.can_login(username="administrator", password="admin")
    app.session.login(user_name="administrator", user_pass="admin")
    assert app.session.is_logged_in_as("administrator")
    #open create page
    app.open_create_page()
    # fill form
    pn = "name0"
    pd = "desc0"
    app.fill_form(pname=pn, pdesc=pd)
    # check creation
    wd.find_element_by_xpath("//a[@href='/mantisbt-2.25.2/manage_overview_page.php']").click()
    wd.find_element_by_link_text(u"Управление проектами").click()
    tab = wd.find_element_by_css_selector("table")
    hrefs = tab.find_elements_by_css_selector("a")
    flag = 0
    for i in hrefs:
        if i.text == pn:
            flag = 1
    assert flag == 1
    app.soap.get_projects(username="administrator", password="admin", pname=pn)
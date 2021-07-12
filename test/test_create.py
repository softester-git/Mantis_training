def test_create(app):
    wd = app.wd
    app.session.login(user_name="administrator", user_pass="admin")
    assert app.session.is_logged_in_as("administrator")
    #open create page
    app.open_create_page()
    # fill form
    app.fill_form(pname="name0", pdesc="desc0")
    # check creation
    wd.find_element_by_xpath("//a[@href='/mantisbt-2.25.2/manage_overview_page.php']").click()
    wd.find_element_by_link_text(u"Управление проектами").click()
    tab = wd.find_element_by_css_selector("table")
    hrefs = tab.find_elements_by_css_selector("a")
    flag = 0
    for i in hrefs:
        if i.text == "name1":
            flag = 1
    assert flag == 1
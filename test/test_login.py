def test_login(app):
    app.session.login(user_name="administrator", user_pass="root")
    #assert app.session.is_logged_in_as("administrator")

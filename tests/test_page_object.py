import pytest

from .pageobjects.swag_labs_login_page import SwagLabsLoginPage

def test_open():
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)
    current_url = login_page.get_current_url()

    assert current_url == url_to_open

    login_page.quit()

def test_click_on():
    username = "standard_user"
    password = "secret_sauce"
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)
    login_page.login(username, password)

    assert login_page.get_current_url() != url_to_open

    login_page.quit()

def test_type_into():
    username = "test_user"
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)
    login_page.input_username(username)
    username_field_value = login_page.get_username_field_value()

    assert username_field_value == username

    login_page.quit()

def test_clear():
    username = "test_user"
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)
    login_page.input_username(username)
    login_page.clear_username_field()
    username_field_value = login_page.get_username_field_value()

    assert username_field_value == ""

    login_page.quit()

def test_get_text():
    standard_username = "standard_user"
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)
    
    credentials_text = login_page.get_login_credentials_text()

    assert standard_username in credentials_text

    login_page.quit()

def test_find_elements_by_class_name():
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)

    elements = login_page.find_elements_by(class_name="login_logo")
    assert len(elements) > 0

    login_page.quit()

def test_find_elements_by_css():
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)

    elements = login_page.find_elements_by(css=".login_wrapper")
    assert len(elements) > 0

    login_page.quit()

def test_find_elements_by_id():
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)

    elements = login_page.find_elements_by(id="login-button")
    assert len(elements) > 0

    login_page.quit()

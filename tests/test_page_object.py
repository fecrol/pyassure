import pytest

from .pageobjects.swag_labs_login_page import SwagLabsLoginPage

def test_open():
    url_to_open = "https://www.saucedemo.com/"
    login_page = SwagLabsLoginPage()
    login_page.open(url_to_open)
    current_url = login_page.get_current_url()

    assert current_url == url_to_open

    login_page.quit()

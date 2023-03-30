from pyassure.pagefactory import PageObject

class SwagLabsLoginPage(PageObject):

    find_by = {
        "username_field": ("id", "user-name"),
        "password_field": ("id", "password"),
        "login_btn": ("css", "input[data-test='login-button']"),
        "credentials": ("id", "login_credentials")
    }

    def input_username(self, username:str):
        self.wait_until_clickable(self.username_field)
        self.type_into(self.username_field, username)
    
    def input_password(self, password:str):
        self.wait_until_clickable(self.password_field)
        self.type_into(self.password_field, password)
    
    def click_login_btn(self):
        self.wait_until_clickable(self.login_btn)
        self.click_on(self.login_btn)
    
    def login(self, username:str, password:str):
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()
    
    def get_username_field_value(self):
        return self.username_field.get_attribute("value")
    
    def clear_username_field(self):
        self.clear(self.username_field)
    
    def get_login_credentials_text(self):
        self.wait_until_visible(self.credentials)
        return self.get_text(self.credentials)

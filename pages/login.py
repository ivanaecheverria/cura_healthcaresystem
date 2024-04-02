from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_INPUT = (By.ID, 'txt-username')
    PASSWORD_INPUT = (By.ID, 'txt-password')
    BUTTON_LOGIN = (By.ID, 'btn-login')

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods
    def username_input(self, username):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

    def password_input(self, password):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element(*self.BUTTON_LOGIN)
        login_button.click()



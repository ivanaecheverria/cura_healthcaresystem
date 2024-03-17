"""This module contains the main page of CURA Healthsystem
the page object for the Cura healthcare system page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CuraMainpage:

    URL = 'https://katalon-demo-cura.herokuapp.com/'

    MAKE_APPOINTMENTBUTTON = (By.ID, 'btn-make-appointment')

    def __init__(self, browser):
        self.browser = browser

    #Interaction methods
    #Load url

    def load(self):
        self.browser.get(self.URL)

    def click_make_an_appointment_button(self):
        click_make_an_appointment_button = self.browser.find_element(*self.MAKE_APPOINTMENTBUTTON)
        click_make_an_appointment_button.click()


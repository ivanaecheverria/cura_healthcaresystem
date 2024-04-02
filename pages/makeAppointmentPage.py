from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from datetime import time

class MakeAnAppointmentPage:
    FACILITY_DROPDOWN = (By.CLASS_NAME, 'form-control')
    HOSPITAL_READMISSION_CHECKBOX = (By.ID, 'chk_hospotal_readmission')
    RADIO_INLINE_LIST = (By.NAME, 'programs')
    VISIT_DATE_BUTTON = (By.CLASS_NAME, 'input-group-addon')
    DATE_PICKER_NEXT_BTN = (By.XPATH, '/html/body/div/div[1]/table/thead/tr[2]/th[3]')
    DATEPICKER_DATE_BTN = (By.CLASS_NAME, '<td class="day">22</td>')
    COMMENT_BOX = (By.ID, 'txt_comment')
    BOOK_APPOINTMENT_BUTTON = (By.ID, 'btn-book-appointment')
    TITLE_HEADER = (By.TAG_NAME, 'h2')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def get_header_name(self):
        header = (self.browser.find_element(*self.TITLE_HEADER))
        value = header.get_attribute("value")
        return value

    def choose_facility(self, text):
        facility_dropdown = (self.browser.find_element(*self.FACILITY_DROPDOWN))
        select = Select(facility_dropdown)
        select.select_by_visible_text(text)

    def apply_for_hospital_readmission_checkbox(self):
        apply_for_hospital_readmission_checkbox = (self.browser.find_element(*self.HOSPITAL_READMISSION_CHECKBOX))
        apply_for_hospital_readmission_checkbox.click()

    def choose_healthcare_program(self, radio_inline_button):
        radio_inline_list = (self.browser.find_elements(*self.RADIO_INLINE_LIST))
        for rbutton in radio_inline_list:
            rbutton_t = rbutton.get_attribute("value")
            if rbutton_t == radio_inline_button:
                rbutton.click()

    def visit_day_by_date_picker(self):
        date_picker_button = (self.browser.find_element(*self.VISIT_DATE_BUTTON))
        date_picker_button.click()
        time.sleep(3)






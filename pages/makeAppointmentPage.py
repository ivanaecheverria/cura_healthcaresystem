from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class MakeAnAppointmentPage:
    FACILITY_DROPDOWN = (By.CLASS_NAME, 'form-control')
    HOSPITAL_READMISSION_CHECKBOX = (By.ID, 'chk_hospotal_readmission')
    RADIO_INLINE_MEDICAID = (By.ID, 'radio_program_medicaid')
    VISIT_DATE_BUTTON = (By.CLASS_NAME, 'input-group-addon')
    VISIT_DATE_DATEPICKER = (By.CLASS_NAME, '<td class="day">22</td>')
    COMMENT_BOX = (By.ID, 'txt_comment')
    BOOK_APPOINTMENT_BUTTON = (By.ID, 'btn-book-appointment')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def choose_facility(self, text):
        facility_dropdown = (self.browser.find_element(*self.FACILITY_DROPDOWN))
        select = Select(facility_dropdown)
        select.select_by_visible_text(text)

    def apply_for_hospital_readmission_checkbox(self):
        apply_for_hospital_readmission_checkbox = (self.browser.find_element(*self.HOSPITAL_READMISSION_CHECKBOX))
        apply_for_hospital_readmission_checkbox.click()


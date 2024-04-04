"""These tests cover the functionality to Make an Appointment"""
import time
from pages.mainPage import CuraMainpage
from pages.login import LoginPage
from pages.makeAppointmentPage import MakeAnAppointmentPage


def test_make_an_appointment(browser):
    #Instance the main, login and make an appointment pages

    main_page = CuraMainpage(browser)
    login_page = LoginPage(browser)
    make_an_appointment_page = MakeAnAppointmentPage(browser)
    USERNAME = 'John Doe'
    PASSWORD = 'ThisIsNotAPassword'
    FACILITY = ['Tokyo CURA Healthcare Center','Hongkong CURA Healthcare Center', 'Seoul CURA Healthcare Center']
    HEALTHCARE_PROGRAM = ['Medicare','Medicaid','None']
    EXPECTED_HEADER: str = "Make Appointment"


    #Given the Cura Main page is displayed

    main_page.load()

    #When the user clicks on the Make An Appointment Button

    main_page.click_make_an_appointment_button()
    browser.implicitly_wait(10)

    #Then the Login page is displayed and the user enter their credentials

    login_page.username_input(USERNAME)
    login_page.password_input(PASSWORD)

    #And the user clicks Login button

    login_page.click_login_button()
    browser.implicitly_wait(20)

    #Then the Make an appointment page is displayed
    ACTUAL_HEADER = make_an_appointment_page.get_header_name()
    assert  str(ACTUAL_HEADER) == str(EXPECTED_HEADER)

    #Then the user chooses a Facility from the dropdown menu

    make_an_appointment_page.choose_facility(FACILITY[2])

    #And the user clicks on the 'Apply for hospital readmission checkbox

    make_an_appointment_page.apply_for_hospital_readmission_checkbox()

    #And the user chooses Medicaid from the Healthcare Program inline radio

    make_an_appointment_page.choose_healthcare_program(HEALTHCARE_PROGRAM[2])
    time.sleep(10)

    #And the user clicks on the calendar icon

    #And the user selects a date from the calendar day picker

    #And the user inputs text in the Comment textbox

    #And the user clicks on the Book Appointment button

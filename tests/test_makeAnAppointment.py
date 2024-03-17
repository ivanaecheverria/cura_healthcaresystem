"""These tests cover the functionality to Make an Appointment"""

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
    FACILITY = 'Hongkong CURA Healthcare Center'

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
    browser.implicitly_wait(10)

    #Then the Make an appointment page is displayed
    #And the user choses a Facility from the dropdown menu

    make_an_appointment_page.choose_facility(FACILITY)

    #And the user clicks on the 'Apply for hospital readmission checkbox

    make_an_appointment_page.apply_for_hospital_readmission_checkbox()

    #And the user choses Medicaid from the Healthcare Program inline radio

    #And the user clicks on the calendar icon

    #And the user selects a date from the calendar daypicker

    #And the user inputs text in the Comment textbox

    #And the user clicks on the Book Appointment button

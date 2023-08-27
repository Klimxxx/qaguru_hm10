
from selene import be, have, browser, command
from selene.support.shared import browser
import os

class RegistrationPage:

    def __init__(self):
        self.name = browser.element('[id=firstName]')
        self.lastname = browser.element('[id=lastName]')
        self.email = browser.element('[id=userEmail]')
        self.gender = browser.element('[id^=gender-radio][value=Female]+label')
        self.phone = browser.element('[id=userNumber]')
        self.year_birthday = browser.element('#dateOfBirthInput')
        browser.element('select[class^=react-datepicker__year]')
        self.month_birthday = browser.element('.react-datepicker__month-select')
        self.day_birthday = browser.element(f'[aria-label= "Choose Monday, January 2nd, 1989"]')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element(f'[id="hobbies-checkbox-2"]+label')

        self.address = browser.element('[id=currentAddress]')
        self.state = browser.element('#state').perform(command.js.scroll_into_view).click().all(
        '[id^=react-select][id*=option]').element_by(have.exact_text('NCR'))
        self.city = browser.element('#city').click()
        browser.element('[id="react-select-4-option-0"]')
        self.submit_button = browser.element('#submit')




        self.should_registered_user_data = browser.element('.table').all('td')

    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')

    def fill_first_name(self, value):
        self.name.should(be.blank).type(value)

    def fill_last_name(self, value):
        self.lastname.should(be.blank).type(value)

    def fill_email(self, value):
        self.email.should(be.blank).type(value)

    def choose_gender(self):
        self.gender.click()

    def fill_phone(self, value):
        self.phone.should(be.blank).type(value)


    def choose_birthday_date(self):
        browser.element('#dateOfBirthInput').click()

    def choose_year_of_birth(self, year):
        self.year_birthday(browser.element('select[class^=react-datepicker__year]').send_keys(year))

    def choose_month_of_birth(self, month):
        self.year_birthday(browser.element('.react-datepicker__month-select').send_keys(month)).click()

    def choose_day_of_birth(self, day):
        self.year_birthday(browser.element(f'[aria-label= "Choose Monday, January {day}nd, 1989"]').send_keys(day)).click()

    def choose_subjects(self, value):
        self.subjects.send_keys(value)
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def choose_hobby_and_scroll(self):
        self.hobbies.perform(command.js.scroll_into_view).click()

    def uploadpicture(self, image):
        return browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, f'resources/{image}')))

    def fill_address(self, value):
        self.address.should(be.blank).type(value)

    def choose_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view).click().all(
            '[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def choose_city(self):
        browser.element('#city').click()
        return browser.element('[id="react-select-4-option-0"]').click()

    def submit(self):
        return browser.element('#submit').click()



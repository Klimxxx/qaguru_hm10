from selene import be, have, browser, command
from selene.support.shared import browser
import os

from qaguru_hm10.pages.user import User


class RegistrationPage:

    def __init__(self):
        self.name = browser.element('[id=firstName]')
        self.lastname = browser.element('[id=lastName]')
        self.email = browser.element('[id=userEmail]')
        self.gender = browser.element('[id^=gender-radio][value=Female]+label')
        self.phone = browser.element('[id=userNumber]')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('[id="hobbies-checkbox-2"]+label')
        self.address = browser.element('[id=currentAddress]')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.should_registered_user_data = browser.element('.table').all('td')

    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')

    def fill_first_name(self, User):
        self.name.should(be.blank).type(User.first_name)

    def fill_last_name(self, User):
        self.lastname.should(be.blank).type(User.last_name)

    def fill_email(self, User):
        self.email.should(be.blank).type(User.email)

    def choose_gender(self):
        self.gender.click()

    def fill_phone(self, User):
        self.phone.should(be.blank).type(User.phone)


    def choose_birthday_date(self, User):
        browser.element('#dateOfBirthInput').click()
        browser.element('select[class^=react-datepicker__year]').send_keys(User.date_birth[0])
        browser.element('.react-datepicker__month-select').send_keys(User.date_birth[1])
        browser.element(f'[aria-label= "Choose Monday, January {User.date_birth[2]}nd, 1989"]').click()


    def choose_subjects(self, User):
        self.subjects.send_keys(User.subjects)
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(User.subjects)).click()

    def choose_hobby_and_scroll(self):
        self.hobbies.perform(command.js.scroll_into_view).click()

    def uploadpicture(self):
        return browser.element('#uploadPicture').set_value(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'resources/image.png')))


    def fill_address(self, User):
        self.address.should(be.blank).type(User.address)

    def choose_state(self, User):
        self.state.perform(command.js.scroll_into_view).click().all('[id^=react-select][id*=option]').element_by(have.exact_text(User.state)).click()

    def choose_city(self):
        self.city.click()
        browser.element('[id="react-select-4-option-0"]').click()

    def submit(self):
        self.submit_button.click()


    def register(self, User):
        self.fill_first_name(User)
        self.fill_last_name(User)
        self.fill_email(User)
        self.choose_gender()
        self.fill_phone(User)
        self.choose_birthday_date(User)
        self.choose_subjects(User)
        self.choose_hobby_and_scroll()
        self.uploadpicture()
        self.fill_address(User)
        self.choose_state(User)
        self.choose_city()
        self.submit()

    def should_have_registered()
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

    @property
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')

    def fill_first_name(self, user: User):
        self.name.should(be.blank).type(user.first_name)

    def fill_last_name(self, user: User):
        self.lastname.should(be.blank).type(user.last_name)

    def fill_email(self, user: User):
        self.email.should(be.blank).type(user.email)

    def choose_gender(self):
        self.gender.click()

    def fill_phone(self, user: User):
        self.phone.should(be.blank).type(user.phone)


    def choose_birthday_date(self, user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element('select[class^=react-datepicker__year]').send_keys(user.date_birth[0])
        browser.element('.react-datepicker__month-select').send_keys(user.date_birth[1])
        browser.element(f'[aria-label= "Choose Monday, January {user.date_birth[2]}nd, 1989"]').click()


    def choose_subjects(self, user: User):
        self.subjects.send_keys(user.subjects)
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.subjects)).click()

    def choose_hobby_and_scroll(self):
        self.hobbies.perform(command.js.scroll_into_view).click()

    def uploadpicture(self):
        return browser.element('#uploadPicture').set_value(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'resources/image.png')))


    def fill_address(self, user: User):
        self.address.should(be.blank).type(user.address)

    def choose_state(self, user: User):
        self.state.perform(command.js.scroll_into_view).click().all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()

    def choose_city(self):
        self.city.click()
        browser.element('[id="react-select-4-option-0"]').click()

    def submit(self):
        self.submit_button.click()


    def register(self, user: User):
        self.fill_first_name(user)
        self.fill_last_name(user)
        self.fill_email(user)
        self.choose_gender()
        self.fill_phone(user)
        self.choose_birthday_date(user)
        self.choose_subjects(user)
        self.choose_hobby_and_scroll()
        self.uploadpicture()
        self.fill_address(user)
        self.choose_state(user)
        self.choose_city()
        self.submit()

    def should_have_registered(self, user: User):
        self.should_registered_user_data.should(have.texts(
        'Student Name', f'{user.first_name} {user.last_name}',
        'Student Email', f'{user.email}',
        'Gender', f'{user.gender}',
        'Mobile', f'{user.phone}',
        'Date of Birth', f'{user.date_birth[2]} {user.date_birth[1]},{user.date_birth[0]}',
        'Subjects', f'{user.subjects}',
        'Hobbies', f'{user.hobbies}',
        'Picture', f'{user.image}',
        'Address', f'{user.address}',
        'State and City', f'{user.state} {user.city}'
    ))

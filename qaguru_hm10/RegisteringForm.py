# from selene import browser, be, have, command
# from selene.support.shared import browser
# from qaguru_hm10 import User
#
# class RegisteringForm:
#
#     def start_test(self, user):
#         self.fill(user)
#         self.submit()
#         self.shouldBeSucceed(user)
#
#     def fill(self, user):
#         self.open_browser()
#         self.fill_first_name(user.first_name)
#         self.fill_last_name(user.last_name)
#         self.fill_email(user.email)
#         self.fill_gender(user.gender)
#         self.fill_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
#         self.fill_phone(user.phone)
#
#
#     def submit(self):
#         return browser.element('#submit').click()
#
#     def shouldBeSucceed(self, user):
#         browser.element('.table').all('td').should(have.texts(
#             'Student Name', user.first_name,
#             'Student Email', user.email,
#             'Gender', user.gender
#             # need to proceed with all the data
#         ))
#
#     def open_browser(self):
#         browser.open('/automation-practice-form')
#         browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
#
#     def fill_first_name(self, value):
#         browser.element('[id=firstName]').should(be.blank).type(value)
#
#     def fill_last_name(self, value):
#         browser.element('[id=lastName]').should(be.blank).type(value)
#
#     def fill_email(self, value):
#         browser.element('[id=userEmail]').should(be.blank).type(value)
#
#     def fill_gender(self, value):
#         browser.element(f'[id^=gender-radio][value={value}]+label').click()
#
#     def fill_phone(self, value):
#         browser.element('[id=userNumber]').should(be.blank).type(value)
#
#     def fill_date_of_birth(self, year, month, day):
#         browser.element('#dateOfBirthInput').click()
#         browser.element('select[class^=react-datepicker__year]').send_keys(year)
#         browser.element('.react-datepicker__month-select').send_keys(month)
#         browser.element(f'[aria-label= "Choose Monday, January {day}nd, 1989"]').click()
#
#     def choose_subjects(self, value):
#         browser.element('#subjectsInput').send_keys(value)
#         browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
#
#     def choose_hobby_and_scroll(self, value):
#         browser.element(f'[id="hobbies-checkbox-{value}"]+label').perform(command.js.scroll_into_view).click()
#
#     @property
#     def uploadpicture(self):
#         return browser.element('#uploadPicture')
#
#     def fill_address(self, value):
#         browser.element('[id=currentAddress]').should(be.blank).type(value)
#
#     def choose_state(self, value):
#         browser.element('#state').perform(command.js.scroll_into_view).click().all(
#             '[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
#
#     def choose_city(self):
#         browser.element('#city').click()
#         return browser.element('[id="react-select-4-option-0"]').click()

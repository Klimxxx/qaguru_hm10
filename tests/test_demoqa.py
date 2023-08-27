from selene import have, browser
from selene.support.shared import browser

from qaguru_hm10.pages.user import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name("Elena")
    registration_page.fill_last_name("Pirogova")
    registration_page.fill_email('123@123.ru')
    registration_page.choose_gender()
    registration_page.fill_phone('8987654321')
    registration_page.choose_birthday_date()
    registration_page.choose_year_of_birth('1989')
    registration_page.choose_month_of_birth('January')
    registration_page.choose_day_of_birth('2')
    registration_page.choose_subjects('English')
    registration_page.choose_hobby_and_scroll()
    registration_page.uploadpicture('image.png')
    registration_page.fill_address('Kazakhstan')


    # штат, город, submit
    # browser.element('#state').perform(command.js.scroll_into_view).click().all(
    #     '[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    # browser.element('#city').click()
    # browser.element('[id="react-select-4-option-0"]').click()
    # browser.element('#submit').click()

    # проверяем успешность регистрации
    browser.element('.table').all('td').should(have.texts(
        'Student Name', 'Elena Pirogova',
        'Student Email', '123@123.ru',
        'Gender', 'Female',
        'Mobile', '8987654321',
        'Date of Birth', '2 January,1989',
        'Subjects', 'English',
        'Hobbies', 'Reading',
        'Picture', 'image.png',
        'Address', 'Kazakhstan',
        'State and City', 'NCR Delhi'
    ))

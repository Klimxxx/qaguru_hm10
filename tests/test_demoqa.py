from selene import have
from qaguru_hm10 import resources
from qaguru_hm10.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    # Имя, Фамилия, Имейл, Пол, номер телефона
    registration_page.fill_first_name('Elena')
    registration_page.fill_last_name('Pirogova')
    registration_page.fill_email('123@123.ru')
    registration_page.choose_gender('Female')
    registration_page.fill_phone('8987654321')
    # дата рождения, год, месяц, день
    registration_page.fill_date_of_birth('1989', 'January', '2')
    # предметы, хобби, картинка, адрес
    registration_page.choose_subjects('English')
    registration_page.choose_hobby_and_scroll('2')
    registration_page.uploadpicture.set_value(resources.resource_path('image.png'))
    registration_page.fill_address('Kazakhstan')
    # штат, город, submit
    registration_page.choose_state('NCR')
    registration_page.choose_city()
    registration_page.submit()
    # проверяем успешность регистрации
    registration_page.should_registered_user_data.should(have.texts(
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

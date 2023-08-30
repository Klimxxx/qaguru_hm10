from selene import have

from qaguru_hm10.pages.registration_page import RegistrationPage
from qaguru_hm10.pages.user import User










def test_student_registration_form():
    registration_page = RegistrationPage()
    elena = User(first_name='Elena', last_name='Pirogova', email='123@123.ru', phone='8987654321',
                 date_birth=['1989', 'January', '2'], subjects='English', address='Kazakhstan', state='NCR')

    registration_page.open()
    registration_page.register(elena)

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

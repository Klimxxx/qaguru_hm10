from qaguru_hm10.pages.registration_page import RegistrationPage
from qaguru_hm10.pages.user import User


def test_student_registration_form():
    registration_page = RegistrationPage()
    elena = User(first_name='Elena', last_name='Pirogova', gender='Female', email='123@123.ru', phone='8987654321',
                 date_birth=['1989', 'January', '2'], subjects='English', hobbies='Reading', address='Kazakhstan',
                 state='NCR', city='Delhi', image='image.png')

    registration_page.open
    registration_page.register(elena)

    registration_page.should_have_registered(elena)

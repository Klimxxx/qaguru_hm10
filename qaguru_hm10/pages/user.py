class User:
    first_name = str
    last_name = str
    email = str
    phone = str
    date_birth = list
    subjects = str
    address = str
    state = str


    def __init__(self, first_name: str, last_name: str, email: str, phone: str, date_birth: list, subjects: str,
                 address: str, state: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.date_birth = date_birth
        self.subjects = subjects
        self.address = address
        self.state = state


# elena = User(first_name='Elena', last_name ='Pirogova', email='123@123.ru', phone='8987654321', date_birth=['1989', 'January', '2'], subjects='English', address='Kazakhstan', state='NCR')
#
# print(str(elena.date_birth))
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    gender: str
    email: str
    phone: str
    date_birth: list
    subjects: str
    hobbies: str
    address: str
    state: str
    city: str
    image: str

    # def __init__(self, first_name: str, last_name: str, gender: str, email: str, phone: str, date_birth: list, subjects: str, hobbies: str,
    #              address: str, state: str, city: str, image: str):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.gender = gender
    #     self.email = email
    #     self.phone = phone
    #     self.date_birth = date_birth
    #     self.subjects = subjects
    #     self.hobbies = hobbies
    #     self.address = address
    #     self.state = state
    #     self.city = city
    #     self.image = image





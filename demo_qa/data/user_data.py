from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    address: str
    gender: str
    birth_year: str
    birth_month: str
    birth_day: int
    subject: str
    hobby: str
    avatar: str
    state: str
    city: str


test_user = User(first_name='Maks',
                 last_name='Kudaev',
                 email='example@gmail.com',
                 mobile='7999999999',
                 address='India',
                 gender='Female',
                 birth_year='2000',
                 birth_month='April',
                 birth_day=10,
                 subject='Arts',
                 hobby='Sports',
                 avatar='photo.jpg',
                 state='Uttar Pradesh',
                 city='Agra')

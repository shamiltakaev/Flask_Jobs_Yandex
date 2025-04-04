from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/mars_explorer_.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Адамов"
    user.name = "Муслим"
    user.age = 21
    user.position = "Капитан"
    user.speciality = "Инженер исследователь"
    user.address = "Модуль_1"
    user.email = "adamov_1@mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Муслимов"
    user.name = "Адам"
    user.age = 18
    user.position = "Главный научный сотрудник"
    user.speciality = "Геолог"
    user.address = "Модуль_1"
    user.email = "muslimov_1@mars.org"
    user.hashed_password = "sci"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Хадисов"
    user.name = "Амхад"
    user.age = 25
    user.position = "Ученый"
    user.speciality = "Биолог"
    user.address = "Модуль_2"
    user.email = "hadisov_1@mars.org"
    user.hashed_password = "bio"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Юсупов"
    user.name = "Вахид"
    user.age = 15
    user.position = "Пилот"
    user.speciality = "Пилот, штурман"
    user.address = "Модуль_2"
    user.email = "yusupov_1@mars.org"
    user.hashed_password = "pilot"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Газиев"
    user.name = "Эртугрул"
    user.age = 27
    user.position = "Программист"
    user.speciality = "ИТ специалист"
    user.address = "Модуль_2"
    user.email = "gaziev_1@mars.org"
    user.hashed_password = "comp"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Умаров"
    user.name = "Ибрагим"
    user.age = 17
    user.position = "Главный инженер"
    user.speciality = "Строитель"
    user.address = "Модуль_1"
    user.email = "umarov_1@mars.org"
    user.hashed_password = "build"

    user.set_password(user.hashed_password)
    
    user = User()
    user.surname = "Азизов"
    user.name = "Умар"
    user.age = 17
    user.position = "Доктор"
    user.speciality = "Доктор"
    user.address = "Модуль_1"
    user.email = "azizov_1@mars.org"
    user.hashed_password = "build"

    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()

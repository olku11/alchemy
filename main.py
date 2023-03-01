from flask import Flask
from data import db_session
from data.users import *
from data.jobs import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    session.add(user)
    session.commit()
    user = User()
    user.surname = 'Dwayne Douglas'
    user.name = 'Johnson'
    user.age = 50
    user.position = 'Spy'
    user.speciality = 'Rock'
    user.address = 'module_2'
    user.email = 'imnotspy@illuminati.by'
    session.add(user)
    session.commit()
    user = User()
    user.surname = 'Jason'
    user.name = 'Statham'
    user.age = 55
    user.position = 'cleaner'
    user.speciality = 'cleaner'
    user.address = 'module_3'
    user.email = 'badboy@illuminati.kz'
    session.add(user)
    session.commit()
    user = User()
    user.surname = 'Arnold'
    user.name = 'Schwarzenegger'
    user.age = 75
    user.position = 'soldier'
    user.speciality = 'terminator'
    user.address = 'module_4'
    user.email = 'california@illuminati.tv'
    session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()
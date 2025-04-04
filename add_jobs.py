from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer_.db")
    session = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = 'Развертывание жилых модулей 1 и 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'Исследование минеральных ресурсов'
    job.work_size = 15
    job.collaborators = '4, 3, 6'
    job.is_finished = True

    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'Разработка систему управления'
    job.work_size = 25
    job.collaborators = '5'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 4
    job.job = 'Анализ атмосферы'
    job.work_size = 15
    job.collaborators = '4, 5'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 5
    job.job = 'Техническое обслуживание марсохода'
    job.work_size = 5
    job.collaborators = '4'
    job.is_finished = True

    session.add(job)

    job = Jobs()
    job.team_leader = 7
    job.job = 'Профилактические процедуры экипажа'
    job.work_size = 7
    job.collaborators = '3'
    job.is_finished = False

    session.add(job)

    session.commit()


if __name__ == '__main__':
    main()

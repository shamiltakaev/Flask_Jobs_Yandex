from data.users import User
from data import db_session
from flask import Flask, render_template
from data.jobs import Jobs
from flask import Flask, redirect, render_template
from forms import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template("index.html", jobs=jobs, names=names)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


def main():
    db_session.global_init("db/mars_explorer_.db")
    app.run(debug=True)


if __name__ == '__main__':
    main()

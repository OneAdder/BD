from flask import Flask, render_template, request, url_for, redirect, flash, abort
from flask_mail import Mail, Message
import sqliter

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/show')
def show_table():
    data = sqliter.show_all()
    return render_template('show.html', table = data)

@app.route('/add_worker')
def add_worker():
    if 'name' in request.args:
        argus = ['name', 'patronymic', 'surename']
        check = True
        for ar in argus:
            if ar not in request.args:
                check = False
                flash('You forgot ' + ar)
        if not check:
            return redirect(url_for('add_worker'))

        if sqliter.add_worker(request.args) == 1:
            return redirect(url_for('add_worker', message = 'No rooms available. Rent a bigger office'))
        return redirect(url_for('main_page', message = 'Added successfully'))
    else:
        return render_template('add_worker.html')



app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'databaseshse@gmail.com'
app.config['MAIL_PASSWORD'] = 'absolutely_secret'
app.config['MAIL_DEBUG'] = True
mail = Mail(app)
app.config.from_object(__name__)
app.config['ADMINS'] = ['databaseshse@gmail.com']

@app.route('/')
def main_page():
    message = ''
    with open('.secret_config', 'r', encoding = 'UTF-8') as f:
        check = f.read()
    if check != 'afklhsdfd\n':
        print(check)
        return 'a'
        message = 'Вы начали проверять моё дз. Информация об этом отправлена мне на почту, а так же вам на почту eklyshinsky@hse.ru'
        email = request.form['email']
        sender = request.form['person']
        msg = Message(message, sender=app.config['ADMINS'][0], recipients = ['mikivo@list.ru'])
        msg.body = message
        mail.send(msg)
        with open('.secret_config', 'w', encoding = 'UTF-8') as f:
            check = f.write('')
    return render_template('main.html', message = message)

@app.route('/coffee')
def teapot():
    abort(418)

if __name__ == '__main__':
    app.run()

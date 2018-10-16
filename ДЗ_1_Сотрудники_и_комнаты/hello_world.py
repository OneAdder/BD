from flask import Flask, render_template, request, url_for, redirect, flash, abort
from flask_mail import Mail, Message
import sqliter

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/show')
def show_table():
    data = sqliter.show_all()
    return render_template('show.html', table = data)

@app.route('/add_worker', methods=['GET', 'POST'])
def add_worker():
    if request.method == 'POST':
        message = ''
        check = True
        if not request.form['name']:
            check = False
            message += 'Вы забыли имя<br>'
        if not request.form['patronymic']:
            check = False
            message += 'Вы забыли отчество<br>'
        if not request.form['surename']:
            check = False
            message += 'Вы забыли фамилию<br>'
        if not check:
            return render_template('add_worker.html', message = message)
        '''
        argus = ['name', 'patronymic', 'surename']
        check = True
        for ar in argus:
            if not request.form['ar']:
                message = 'asdfgsdf'
        if not check:
            return redirect('/')
        '''
        if sqliter.add_worker(request.form) == 1:
            return redirect(url_for('main_page', message = 'Нет свободных комнат. Найдите офис побольше'))
        return render_template('add_worker.html', message = 'Успешно добавлен')
    else:
        return render_template('add_worker.html')


@app.route('/delete=<i>')
def delete_worker(i):
    sqliter.delete_worker(i)
    return redirect(url_for('main_page'))


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'databeseshse@gmail.com'
app.config['MAIL_PASSWORD'] = 'absolutely_secret'
app.config['MAIL_DEBUG'] = True
mail = Mail(app)
app.config.from_object(__name__)
app.config['ADMINS'] = ['databeseshse@gmail.com']

@app.route('/')
def main_page():
    message = ''
    with open('.secret_config', 'r', encoding = 'UTF-8') as f:
        check = f.read()
    if check != 'afklhsdfd\n':
        message = 'Проверка пошла'
        msg = Message(message, sender=app.config['ADMINS'][0], recipients = ['mikivo@list.ru'])
        msg.body = message
        mail.send(msg)
        with open('.secret_config', 'w', encoding = 'UTF-8') as f:
            check = f.write('afklhsdfd\n')
        return render_template('main.html', message = 'Вы начали проверять моё дз. Информация об этом отправлена мне на почту')
    else:
        return render_template('main.html', message = '')

@app.route('/coffee')
def teapot():
    abort(418)

if __name__ == '__main__':
    app.run()

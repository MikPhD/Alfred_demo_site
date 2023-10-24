import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)


app = Flask(__name__)
used_ids = ['123', '456', '789']
@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/submit', methods=['POST'])
def submit():
    input_value = request.form.get('id')
    print("Valore del campo di input:", input_value)
    return redirect(url_for('success'))
#
@app.route('/check_id', methods=['POST'])
def check_id():
    input_value = request.form.get('id')

    if input_value in used_ids:
        return jsonify({'valid': False})
    else:
        return jsonify({'valid': True})
#
#
@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()

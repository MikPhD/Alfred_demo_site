import os
import mysql.connector
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)


app = Flask(__name__)
# Define the MySQL database connection
cnx = mysql.connector.connect(user="Alfred", password="b0t1qu3m3!", host="alfred-database.mysql.database.azure.com", port=3306,
                              database="mysql", ssl_ca="./certificate.pem", ssl_disabled=False)

# Create a function to add the 'id' value to the database
def add_id_to_database(id_value):
    try:
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO id-placeholders (id) VALUES (%s)", (id_value,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    except Exception as e:
        print("Error:", str(e))
        return False

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
    add_id_to_database(input_value)
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

import os
import mysql.connector
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)
from datetime import datetime
from time import sleep


app = Flask(__name__)
# Define the MySQL database connection


def add_registration_to_database(reg_time, id, wifi_pass, address, hot_water_solution, pool_price, breakfast):
    try:
        cnx = mysql.connector.connect(user="Alfred", password="b0t1qu3m3!",
                                      host="alfred-database.mysql.database.azure.com", port=3306,
                                      database="guests", ssl_ca="./certificate.pem")
        cursor = cnx.cursor()

        cursor.execute("INSERT INTO guests.registrations "
                       "(reg_time, id, wifi_pass, address, hot_water_solution, pool_price, breakfast) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)", (reg_time, id, wifi_pass, address, hot_water_solution, pool_price, breakfast))
        cnx.commit()
        cursor.close()
        cnx.close()
        print("done")
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
    reg_time = datetime.now()
    id = request.form.get('id')
    wifi_pass = request.form.get('wifi')
    address = request.form.get('address')
    hot_water_solution = request.form.get('hot_water_solution')
    pool_price = request.form.get('pool_price')
    breakfast = request.form.get('breakfast')

    add_registration_to_database(reg_time, id, wifi_pass, address, hot_water_solution, pool_price, breakfast)
    return redirect(url_for('success'))
#
@app.route('/check_id', methods=['POST'])
def check_id():
    sleep(3)  # Simulate a delay in checking the database
    id_to_check = request.form.get('id')

    # Esegui una query per verificare se l'ID esiste già nel database
    cnx = mysql.connector.connect(user="Alfred", password="b0t1qu3m3!",
                                  host="alfred-database.mysql.database.azure.com", port=3306,
                                  database="guests", ssl_ca="./certificate.pem")

    cursor = cnx.cursor()
    query = "SELECT COUNT(*) FROM registrations WHERE id = %s"
    cursor.execute(query, (id_to_check,))
    count = cursor.fetchone()[0]

    if count > 0:
        # L'ID esiste già nel database
        return jsonify({'valid': False, 'message': 'This ID is already in use'})
    else:
        # L'ID è valido
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


def check_database_connection():
    try:
        # Check if the connection is successful
        if cnx.is_connected():
            print("Connection successful!")

            # Execute a simple query to test the connection
            cursor = cnx.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("Query result:", result)

        else:
            print("Connection failed.")

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        # Close the connection
        cnx.close()
        pass

if __name__ == '__main__':
   app.run(debug=True)

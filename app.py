from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, inspect, insert


app = Flask(__name__)

used_ids = set(["prova"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_value = request.form.get('id')
    print("Valore del campo di input:", input_value)
    return redirect(url_for('success'))

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


app.run()

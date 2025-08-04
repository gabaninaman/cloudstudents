from flask import Flask, render_template, request
import os
import pyodbc

app = Flask(__name__)
server = 'sqlservergiy6qzboazqik.database.windows.net'
driver = '{ODBC Driver 18 for SQL Server}'


database='sampledb';
Uid='cloudadmin';
Pwd='CloudProject132';
Encrypt='yes';
TrustServerCertificate='no';

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={Uid};PWD={Pwd};Encrypt={Encrypt};TrustServerCertificate={TrustServerCertificate}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first = request.form['first']
    last = request.form['last']
    email = request.form['email']

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (FirstName, LastName, Email) VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()

    return render_template('success.html', first=first)

if __name__ == '__main__':
    app.run(debug=True)

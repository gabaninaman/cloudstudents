from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Replace these values with your Azure SQL settings
server = 'sqlservergiy6qzboazqik.database.windows.net'
database = 'sampledb'
username = 'cloudadmin'
password = 'CloudProject132'
driver = '{ODBC Driver 17 for SQL Server}'

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

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

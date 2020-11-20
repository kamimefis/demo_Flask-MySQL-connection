from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'root'
app.config['MYSQL_DB']= 'my_users'

mysql=MySQL(app)

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        details= request.form
        name= details['fname']
        last_name= details['lname']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, last_name) VALUES (%s, %s)", (name, last_name))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')    

if __name__ == '__main__':
    app.run()
from multiprocessing import connection
from click import password_option
from flask import *
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder='templates')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pratham1008'
app.config['MYSQL_DB'] = 'prat'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        username = request.form['Username']
        password = request.form['Password']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO credentials(username, password) VALUES(%s, %s)''', (username, password))
        mysql.connection.commit()
        cursor.close()
        return "<h1> Done </h1>"
    return render_template("html/index.html")

if __name__ == "__main__":
    app.run(debug=True)
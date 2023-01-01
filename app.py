
from flask import *
import mysql.connector


app = Flask(__name__, template_folder='templates')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pratham1008'
app.config['MYSQL_DB'] = 'prat'
app=Flask(__name__)
username=['prat', 'kunal']
password=['prat1008', 'kunal123']
@app.route("/", methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        username = request.form['Username']
        password = request.form['Password']
        for i, j in username, password:
            if i==username and j ==password:
                return "html/home.html"
    return render_template("html/index.html")

if __name__ == "__main__":
    app.run(debug=True)
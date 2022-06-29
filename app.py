from click import password_option
from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        username = request.form('Username')
        password = request.form('Password')
        print(username)
        print(password)
    return render_template("html/index.html")



if __name__ == "__main__":
    app.run(debug=True)
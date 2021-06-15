from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',my_name='Abigail Plata')

@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/looping')
def looping():
    Users={
        "Archie":"Amsterdam",
        "Veronica":"London",
        "Betty":"San Francisco",
        "Jughead":"Los Angeles"
    }
    return render_template("looping.html", users=Users)

users = {
    "joe.blow@email.com": "password123",
    "wendy.blow@email.com": "123password"
}

@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", message = "Successfully Logged In")
        return render_template("login.html", form=form, message="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
    return render_template("login.html", form=form)

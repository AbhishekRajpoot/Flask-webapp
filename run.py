
from flask import Flask, render_template, request, redirect, flash, session, url_for
from firebase_admin import credentials, firestore, initialize_app, auth
import firebase_admin
from firebase_admin import db

app = Flask(__name__)

app.secret_key = "dont tell anyone"

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://caddydatabase.firebaseio.com/Customers"
})

ref = db.reference("/Customer_1")
emp_db = firestore.client()
database = {'admin':'password','employee':'password'}    


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add_emp',methods=['POST','GET'])
def add_emp():
    if request.method == 'POST':
        name=request.form['username']
        email=request.form['email']
        contact=request.form['contact']
        address=request.form['address']
        doc_ref = emp_db.collection('profiles').document(name)
        doc_ref.set({
        'Name':name,
        'Email':email,
        'contact':contact,
        'Address':address
        })
        flash(name + " added successfully","success")
    return redirect('/admin')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =="POST":
        name=request.form['name']
        pwd=request.form['password']
        if name not in database:
            return render_template("index.html", info='Invalid User')
        else:
            if database[name]!=pwd:
                return render_template("index.html", info='Invalid Password')
            else:
                if name == "admin":
                    session['login_state'] =True
                    return render_template("admin.html")
                else:
                    session['login_state'] =True
                    return render_template("employee.html")
    if session.get("login_state") :
        return render_template('admin.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search",methods=['POST','GET'])
def search():
    session['login_state'] =True
    search=request.form['search']
    dt = db.reference("/Customer_" + search)
    data = dt.get().values()
    return render_template("employee.html", data=data)


@app.route("/emp")
def emp():
    return render_template("employee.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
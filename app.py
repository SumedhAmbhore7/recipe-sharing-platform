from flask import *
from flask import Flask,redirect,render_template,request,url_for,session
import os
app=Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'sumedh')

import sqlite3

def db_connect():
    con=sqlite3.connect('reg.db')
    return con

def create_table():
    con=db_connect()
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS information(id INTEGER PRIMARY KEY,user varchar(100),email varchar(100) UNIQUE,contact int(100),password varchar(100))")
create_table()

@app.route("/")
def ro():
    return render_template("home.html")

@app.route("/login",methods=['POST','GET'])
def login():
    # if request.method=='POST':
    #     e=request.form['email']
    #     p=request.form['password']
        
    #     con=db_connect()
    #     c=con.cursor()
        
    #     data=c.execute("SELECT * from information where email=? and password=?",(e,p))
    #     data=c.fetchall()
    #     if data:
    #         return redirect(url_for('home'))
    #     else:
    #         return "It is password failed"
    #         # return "<script>alert(login Failed)</script>"
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/reg_save',methods=['POST'])
def reg_save():
    if request.method=='POST':
        us=request.form['user']
        em=request.form['email']
        co=request.form['contact']
        pa=request.form['password']
        
        con=db_connect()
        c=con.cursor()
        
        c.execute("select * from information")
        data=c.fetchall()
        for i in data:
            if i[2]==em:
                return "<script>alert('Email already exists');location.href='/register'</script>"
        
        c.execute("insert into information(user,email,contact,password) values(?,?,?,?)",(us,em,co,pa))
        con.commit()
        return "<script>window.alert('Registeration Sucessfull');window.location.href='/login'</script>"
    else:
        return redirect(url_for('register'))
    
@app.route("/log_save",methods=['POST'])
def log_save():
    if request.method=='POST':
        e=request.form['email']
        p=request.form['password']

        con=db_connect()
        c=con.cursor()

        data=c.execute("SELECT * from information where email=? and password=?",(e,p))
        for i in data:
            if i[2]==e and i[4]==p:
                session['user'] = i[1]
                # session['email'] = i[2]
                c.execute("CREATE TABLE if not exists '{}' (id INTEGER PRIMARY KEY, recipe_name varchar(100), ingredients varchar(1000), instructions varchar(10000))".format(session['user']))
                return redirect(url_for("home"))
        else:
            # return "It is password failed"
            return "<script>alert('Login Failed')</script>"
    # return redi
    
@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    else:
        return render_template("home.html")

@app.route("/upload_recipe", methods=['POST'])
def upload_recipe():
    if "user" not in session:
        return redirect(url_for("login"))
    else:
        if request.method=='POST':
            t=request.form['title']
            n=request.form['ingredients']
            i=request.form['instructions']
            user=session['user']

            con=db_connect()
            c=con.cursor()
            c.execute(f"insert into '{user}' (recipe_name, ingredients, instructions) values(?,?,?)",(t,n,i))
            con.commit()
            return redirect(url_for('home'))

@app.route("/dashboard")
def dashboard():
    if "user" not  in session:
        return redirect(url_for("login"))
    else:
        return render_template("dashboard.html")

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login"))
    con=db_connect()
    c=con.cursor()
    c.execute("select * from '{}'".format(session['user']))
    data=c.fetchall()

    return render_template("profile.html",data=data)
    
@app.route("/view_recipe/<int:id>")
def view_recipe(id):
    if "user" not in session:
        return redirect(url_for("login"))
    con=db_connect()
    c=con.cursor()
    c.execute("select * from '{}' where id=?".format(session['user']),[id])
    data=c.fetchall()
    
    return render_template("view_recipe.html",data=data)
    
@app.route("/friends")
def friends():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("friends.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)

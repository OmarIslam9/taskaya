from flask import Flask, render_template,request,redirect,url_for
from flask_login import logout_user,current_user

app=Flask(__name__)

data={}

@app.route("/")
def start():
    return render_template("start.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        phone=request.form.get("phone")
        password=request.form.get("password")
        for key in data:
            if phone==key:
                if password==data[key]:
                 return render_template("btn.html")

        return "something went Wrong"

    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        phone=request.form.get("phone")
        print(phone)
        password=request.form.get("password")
        print(password)
        data[phone]=password
        print(data)
        return "registered"


    return render_template("register.html")

@app.route("/logout")
def logout():
    logout_user(current_user)
    return redirect(url_for('start'))




















if __name__==("__main__"):
    app.run(debug=True)
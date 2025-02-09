from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)  # تعریف متغیر app
app.secret_key = "your_secret_key"  # برای مدیریت session


# مسیر لاگین
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # چک کردن یوزر و پسورد
        if username == "admin" and password == "1234":
            session["user"] = username  # ذخیره در session
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password!"

    return render_template("login.html")


# مسیر داشبورد
@app.route('/dashboard')
def dashboard():
    if "user" in session:
        return f"Welcome, {session['user']}! <br><a href='/logout'>Logout</a>"
    else:
        return redirect(url_for('login'))


# مسیر خروج از حساب
@app.route('/logout')
def logout():
    session.pop("user", None)  # حذف session
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=False)

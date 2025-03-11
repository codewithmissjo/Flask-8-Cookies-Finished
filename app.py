from flask import Flask, render_template, request, make_response, redirect
app = Flask(__name__)

@app.route('/')
def index():
  value = request.cookies.get('server-sign-in')
  if value:
    return render_template("index.html", serverStatus=value)
  else:
    return render_template("index.html")  

@app.route('/sign-in', methods=["POST"])
def sign_in():
  value = request.form.get('sign-in')
  resp = make_response(redirect('/'))
  resp.set_cookie('server-sign-in', value, max_age = 300)
  return resp

@app.route('/sign-out')
def sign_out():
  resp = make_response(redirect('/'))
  resp.set_cookie('server-sign-in', "", max_age = 0)
  return resp


if __name__ == '__main__':
  app.run()
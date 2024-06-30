from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
  return render_template("home_sc.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
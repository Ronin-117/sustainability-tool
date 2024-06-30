from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
  return render_template("home.html")

@app.route("/Project_management", methods=['POST', 'GET'])
def Project_management():
  return render_template("project_mang.html")

@app.route("/Project_idea", methods=['POST', 'GET'])
def Project_idea():
  return render_template("project_idea.html")

@app.route("/Material_choosing", methods=['POST', 'GET'])
def Material_choosing():
  return render_template("mat_cho.html")

@app.route("/Credits", methods=['POST', 'GET'])
def Credits():
  return render_template("credits.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
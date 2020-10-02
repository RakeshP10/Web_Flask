from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/aboutus.html")
def aboutus():
    return render_template('aboutus.html')   

@app.route("/contactus.html")
def contactus():
    return render_template('contactus.html')    

app.run(debug=True)
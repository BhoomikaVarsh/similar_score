
from difflib import SequenceMatcher
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

def similar(a, b):

    n = SequenceMatcher(None, a,b).ratio()

    if n > 0.5:

        r = 1

    else:

        r = 0
    
    return r

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/",methods = ['POST'])

def getvalue():

    first = request.form['first']

    second = request.form['second']

    result = similar(first, second)

    return render_template("result.html", r = result)

if __name__ == "__main__":

    app.run(debug= True)

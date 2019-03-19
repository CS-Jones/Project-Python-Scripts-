from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("my_form.html")
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    multiply_text = text * 3
    return multiply_text
if __name__ == '__main__':
    app.run()
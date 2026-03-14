from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1><p>This is your first web app.</p>"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Nice to meet you."

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# A route to the home page of the app
@app.route('/')
def index():
     return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)
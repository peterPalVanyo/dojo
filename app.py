from flask import Flask, redirect

app = Flask(__name__)


counts = 0

@app.route('/request-counter')
def counter():
    global counts
    counts += 1
    return redirect("/")


if __name__ == '__main__':
    app.run(debug= True)

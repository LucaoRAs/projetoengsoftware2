from app import create_app
from flask import Flask, redirect, url_for

app = create_app()

@app.route('/')
def home():
    return redirect(url_for('exame.login_fake'))

if __name__ == '__main__':
    app.run(debug=True) 
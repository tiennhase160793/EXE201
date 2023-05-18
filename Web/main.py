from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact_info():
    return "Ching chong"


if __name__ == '__main__':
    app.run(debug=True)
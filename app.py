from flask import Flask, render_template, url_for, current_app

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/photos')
def photo():
    return render_template('photo.html')

@app.route('/about')
def about(): 
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
    
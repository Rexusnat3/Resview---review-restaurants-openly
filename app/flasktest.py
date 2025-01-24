from flask import Flask, request, jsonify
import reviewer

app = Flask(__name__)

def route_initialization(app):
    @app.route('/')
    def homepage():
        return render_template('Homepage.html')

@app.route('/registerrestaurant'):
def registerrestaurant():
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']


    app.run()